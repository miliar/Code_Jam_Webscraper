#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
#define mod 1000000007




#define T 10 
#define N 1000
#define C 26

int s[T][N][C];
int topo[T];
string in[T];
int n, m;
map <int, int> sz;
int ans;

void add (int no, int trie, int id, int pos){
	//printf("aqui %d %d %d %d\n", no, trie, id, pos);
	if (pos == in[id].size()) return;
   	int x = s[trie][no][in[id][pos]-'A'];
	if (x == -1) s[trie][no][in[id][pos]-'A'] = topo[trie]++;
   	x = s[trie][no][in[id][pos]-'A'];
	add (x, trie, id, pos+1);
}

int onde[N];

void solve (int pos){
	if (pos == m){
		clr (s, -1);
		f (i, 0, n) topo[i] = 1;
		f (i, 0, m) add (0, onde[i], i, 0);
		int ret = 0;
		f (i, 0, n) {
			if (topo[i] != 1)ret += (topo[i]);
		}
		if (ret > ans) ans = ret;
		sz[ret]++;
		return;
	}

	f (i, 0, n){
		onde[pos] = i;
		solve(pos+1);
	}

}


int main (){
	int t; cin >>t;

	f (tt, 1, t+1){
		cin >>m >> n;
		f (i, 0, m) cin >> in[i];
		sz.clear();
		ans = 0;
		solve(0);
		printf("Case #%d: %d %d\n", tt, ans, sz[ans]);
	}
	return 0;
}


