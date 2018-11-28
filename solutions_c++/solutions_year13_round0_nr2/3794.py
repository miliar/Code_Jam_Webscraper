#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define pb push_back
#define mp make_pair
#define sz size()
#define x first
#define y second
#define forn(i, n) for(int i=0; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef pair < int, int > PII;

int k;
int n,m;
int a[110][110];
int p[110][110];

int main()
{
	freopen("z.in", "rt", stdin);
	freopen("z.out", "wt", stdout);

	cin >>k;
	forn(t,k)
	{
		cin >>n>>m;
		forn(i,n)
			forn(j,m)
			{
				scanf("%d",&a[i][j]);
				p[i][j]=100;
			}
		cout <<"Case #"<<t+1<<": ";
		if(n==1 || m==1)
		{
			cout <<"YES"<<endl;
			continue;
		}

		for(int h=100; h>=1; h--)
		{
			forn(i,n)
			{
				bool fl=1;
				forn(j,m)
					if(a[i][j]>h)
						fl=0;
				if(fl)
				{
					forn(j,m)
						p[i][j]=min(p[i][j],h);
				}
			}
			forn(j,m)
			{
				bool fl=1;
				forn(i,n)
					if(a[i][j]>h)
						fl=0;
				if(fl)
				{
					forn(i,n)
						p[i][j]=min(p[i][j],h);
				}
			}
		}

		bool b=1;
		/*
		cout <<endl;
		forn(i,n)
		{
			forn(j,m)
				cout <<a[i][j]<<' ';
			cout <<"   ";
			forn(j,m)
				cout <<p[i][j]<<' ';
			cout <<endl;
		}
		cout <<endl;*/ 
		forn(i,n)
			forn(j,m)
				if(p[i][j]!=a[i][j])
				 	b=0;
		if(b)
			cout <<"YES";
		else
			cout <<"NO";
		cout <<endl;

	}

	return 0;
}
