// b.cpp : Defines the entry point for the console application.
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
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int tnum;
	scanf("%d",&tnum);
	rep(tc,tnum) {
		double c,f,x;
		//scanf("%f %f %f",&c,&f,&x);
		cin >> c>> f >> x;
		printf("Case #%d: ",tc+1);
		double ans = x/2.0;
		double t = x/2.0;
		double del = 2;
		int k = 0;
		double time = 0.0;
		while (true) {
			double needTime = c/del;
			if (time + needTime > ans) break;
			time += needTime;
			del+=f;
			double r = x/del;
			if (time+r < ans) ans = time + r;
		}
		printf("%.9f\n",ans);
	}
	return 0;
}

