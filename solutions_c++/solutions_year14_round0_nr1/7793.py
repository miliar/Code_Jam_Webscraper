// a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <list>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <ctime>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
#define forr(i,a,b) for (int i=a; i<=b; i++)
#define ford(i,a,b) for (int i=a; i>=b; i--)
#define mset(a,b) memset(a,b,sizeof(a))
#define sz(a) int( a.size() )
#define all(A) A.begin(),A.end()
#define sqr(q) q*q
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define X first
#define Y second

typedef long long i64;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef pair<int,int> PII;
typedef vector<string> VS;


int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tnum;
	scanf("%d",&tnum);
	rep(tc,tnum) {
		int u;
		int a[16];
		scanf("%d",&u);
		u--;
		rep(i,16) a[i] = 0;
		rep(i,4)
			rep(j,4) {
				int v;
				scanf("%d",&v);
				v--;
				if (i == u) a[v]++;
			};
		scanf("%d",&u);
		u--;
		rep(i,4)
			rep(j,4) {
				int v;
				scanf("%d",&v);
				v--;
				if (i == u) a[v]++;
			};
		int k=0, v = -1;
		rep(i,16)
			if (a[i] == 2) {
				k++;
				v = i;
			}
			printf("Case #%d: ",tc+1);
		if (k == 0) {
			printf("Volunteer cheated!\n");
		} else if (k == 1) {
			printf("%d\n",v+1);
		} else {
			printf("Bad magician!\n");
		}
	}

	return 0;
}

