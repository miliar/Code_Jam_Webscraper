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

const int N = 2000;

int n;
int a[2][N],t[N];

void printA(int ind) {
	int k = 1<<n;
	rep(i,k) 
		printf("%d ",a[ind][i]);
	printf("\n");
}


void hid(int st, int fin, int ind) {
	if (fin -st <=1) {
		//printf("%d\n",ind);
		return;
	}
	int zn = 1 - ind;
	int p=st;
	for(int i=st; i<fin; i+=2) {
		a[zn][p++] = min(a[ind][i],a[ind][i+1]);
	}

	for(int i=st; i<fin; i+=2) {
		a[zn][p++] = max(a[ind][i],a[ind][i+1]);
	}

	//printA(zn);
	hid(st,(st+fin)/2,zn);
	hid((st+fin)/2,fin,zn);

}


//int n;
int main()
{
	//n=4;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int tnum,p;
	scanf("%d",&tnum);
	rep(tc,tnum) {
		scanf("%d %d",&n,&p);
		rep(i,N) a[0][i]=0,a[1][i] = 0;
		int k = 1<<n;
		rep(i,1<<n) 
			a[0][i] = k-i-1;
		//printA(0);
		hid(0,k,0);
		int minV = 0;
		int maxV = 0;
		int zn = n%2;
		rep(i,p) {
			maxV = max(maxV,a[zn][i]);
			t[ a[zn][i] ] = tc+1;
		}
		while ( t[minV]==tc+1) minV++;
		
		printf("Case #%d: %d %d\n",tc+1,minV-1,maxV);
	}
	
	return 0;
}

