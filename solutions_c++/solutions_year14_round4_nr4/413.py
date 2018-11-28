#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
#include <set>
#include <utility>

#define ALL(v) v.begin(), v.end()

using namespace std;
typedef long long ll;

template< typename T > T next() {  T tmp; cin >> tmp; return tmp; }

void dec(map< int, int > & f, int key) {
	f[key]--;
	if (f[key] == 0) {
		f.erase(key);
	}
}

struct Node {
	Node ** children;
	Node() {
		children = new Node*[26];
		for (int i = 0; i < 26; ++i) {
			children[i] = NULL;
		}
	}
	~Node() {
		for (int i = 0; i < 26; ++i) {
			delete children[i];
		}
		delete[] children;
	}
};

int compute(Node * cur) {
	int size = 1;
	for (int i = 0; i < 26; ++i) {
		if (cur -> children[i] != NULL) {
			size += compute(cur -> children[i]);
		}
	}
	return size;
} 

int nodeNumber(vector< string > const & v) {
	Node * root = new Node();
	for (size_t i = 0; i < v.size(); ++i) {
		Node * cur = root;
		string s = v[i];
		for (int j = 0; j < s.size(); ++j) {
			int let = s[j] - 'A';
			if (cur -> children[let] == NULL) {
				cur -> children[let] = new Node();
			}
			cur = cur -> children[let];
		}
	} 
	int sum = compute(root);
	delete root;
	return sum;
}

void solve() {
	int m = next< int >();
	int n = next< int >();
	vector< string > s(m);
	for (int i = 0; i < m; ++i) {
		s[i] = next< string >();
	}
	int max = -1;
	int reach = 1;

	int minNum = nodeNumber(s);
	vector< string > cv[4];
	int x = 0;
	for (int msk = 0; msk < (1 << (2 * m)); ++msk) {
		for (int i = 0; i < 4; ++i) cv[i].clear();
		bool norm = true;
		for (int i = 0; i < 2 * m; i += 2) {
			int color = (msk >> i) % 2 + 2 * ((msk >> (i + 1)) % 2);
			norm &= color < n;
			cv[color].push_back(s[i / 2]);
		}
		x += norm ? 1 : 0;
		int sum = 0;
		for (int i = 0; i < n; ++i) {
			norm &= !cv[i].empty();
			sum += nodeNumber(cv[i]);
		}
		if (!norm) continue;
		int dec = sum;
		if (max < dec) {
			max = dec;
			reach = 1;
		} else if (max == dec) {
			reach++;
		}
	}
	
	cout << max << " " << reach << endl;
}

int main() {

//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);

  int test = next< int >();
  for (int i = 1; i <= test; ++i) {
  	cerr << i << endl; cerr.flush();
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}

 