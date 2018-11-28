#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cassert>
#include <ctime>

#define Fr(a,b,c) for(int a = b; a < c; ++a)
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define oo 0x3F3F3F3F

#define dbg if(0)

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long rash;

#define MAXN 10
int rows, n, m, k;
int inp[MAXN], ns[MAXN];
set<int> s[2];
bool bt(int lvl, int last) {
	if(lvl == n) {
		s[0].clear();
		s[0].insert(1);
		
		/*
		printf(" < ");
		Fr(i,0,n) printf("%d ", ns[i]);
		puts("");
		//*/
		
		Fr(i,0,n) {
			s[1].clear();
			for(set<int>::iterator it = s[0].begin(); it != s[0].end(); ++it)
				s[1].insert(*it), s[1].insert(*it * ns[i]);
			s[1].swap(s[0]);
		}

		bool ok = true;
		Fr(i,0,k) ok &= s[0].count(inp[i]);
		/*
		if(ok) {
			printf("Ok! %d\n", ok);
			for(set<int>::iterator it = s[0].begin(); it != s[0].end(); ++it) printf(" %d", *it);
			puts("");
		}
		//*/
		return ok;
	}
	
	Fr(i,last,m+1)
		Fr(j,lvl,n) {
			ns[j] = i;
			if(bt(j + 1, i + 1)) return true;
		}
		
	return false;
}

int main() {
	int t; scanf("%d", &t);
	scanf("%d%d%d%d", &rows, &n, &m, &k);
	puts("Case #1:");
	Fr(r,0,rows) {
		Fr(i,0,k) scanf("%d", &inp[i]);
		bt(0, 2);
		Fr(i,0,n) printf("%d", ns[i]); puts("");
	}
	
	return 0;
}


