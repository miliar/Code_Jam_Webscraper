#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<climits>
#include<cassert>
#include<cctype>
#include<ctime>
#include<ciso646>
#include<cstddef>
#include<iostream>
#include<fstream>
#include<functional>
#include<iomanip>
#include<string>
#include<map>
#include<vector>
#include<deque>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
#include<list>
#include<numeric>
#include<complex>
#include<new>

using namespace std;

typedef vector<int> vi;
typedef map<int, int> mii;
typedef set<int> si;
typedef queue<int> qi;
typedef stack<int> sti;
typedef pair<int, int> pii;

namespace Solve {

	template <class T> inline bool _max(T &ans, const T &comp) {
		if (ans < comp) {
			ans = comp;
			return true;
		}
		return false;
	}

	template <class T> inline bool _min(T &ans, const T &comp) {
		if (ans > comp) {
			ans = comp;
			return true;
		}
		return false;
	}

	struct Node {
		Node *next[26];
		Node() { memset(next, 0, sizeof next); }
	};

	class Trie {
		public:
			Node *root;
			int size;
			Trie() {root = new Node(); size = 1;}
			~Trie() { destroy(root); }

			void destroy(Node *cur) {
				for(int i = 0; i < 26; ++ i)
					if(cur -> next[i]) destroy(cur -> next[i]);
				delete cur;
			}

			int insert(Node *cur, const char *str) {
				if(*str == 0) return 0;
				int idx = *str - 'A';
				if(cur -> next[idx] == NULL) {
					cur -> next[idx] = new Node();
					return insert(cur -> next[idx], str + 1) + 1;
				}
				return insert(cur -> next[idx], str + 1);
			}

			void insert(const char *str) {
				size += insert(root, str);
			}

			inline int &getSize() {
				return size;
			}
	};

	int To[8];
	int Ans, Cnt;
	int N, M;
	char String[8][16];
	union LongBool {
		int fastset;
		bool bit[4];
	} ok;
	
	void calc() {
		Trie *data = new Trie[N];
		ok.fastset = 0;
		for(int i = 0; i < M; ++ i) {
			ok.bit[To[i]] = true;
			data[To[i]].insert(String[i]);
		}
		int csize = 0;
		for(int i = 0; i < N; ++ i) {
			if(!ok.bit[i]) return;
			csize += data[i].getSize();
		}
		delete []data;
		if(csize > Ans) {
			Ans = csize, Cnt = 1;
			return;
		}
		if(csize == Ans) ++ Cnt;
	}

	void makeTo(int now) {
		if(now == M) {
			calc();
			return ;
		}
		for(int i = 0; i < N; ++ i) {
			To[now] = i;
			makeTo(now + 1);
		}
	}

	void main(){
		ios_base::sync_with_stdio(false);
		register int i, j;
		int T;
		cin >> T;
		for(int t = 1; t <= T; ++ t) {
			Ans = Cnt = 0;
			memset(String, 0, sizeof String);
			cin >> M >> N;
			for(i = 0; i < M; ++ i) cin >> String[i];
			makeTo(0);
			cout << "Case #" << t << ": " << Ans << " " << Cnt << endl;
		}
	}
}

int main(){
	Solve::main();
	return 0;
}
