//#include "stdafx.h"

#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector>

using namespace std; 

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) fo(i,j,sz(v))
#define Foo(i,j,v) Fo(i,j,sz(v))
#define li(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define CLR(a,v) memset((a),(v),sizeof(a))
#define inf 1000000001
//typedef long long Long;
typedef __int64 Long;
#define pi (2*acos(0))
#define eps 1e-9

#define two(X) (1<<(X))
#define twoL(X) (((Long)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)

char BUFFER[1000000 + 5];
bool readn(int &n)	{ return scanf("%d",&n) == 1; } 
bool readl(Long &n)	{ return scanf("%I64d",&n) == 1; } 
bool readd(double &n){ return scanf("%lf",&n) == 1; } 
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }

int t, n, m;
int x[101][101];

bool IsPossible(int ai, int aj)
{
	bool flag = true;

	for(int i=0;i<n;i++) 
	{
		if(i==ai) continue;
		if(x[ai][aj] < x[i][aj])
		{
			flag = false;
			break;
		}
	}

	if(flag) return flag;
	
	flag = true;

	for(int j=0;j<m;j++) 
	{
		if(j==aj) continue;
		if(x[ai][aj] < x[ai][j])
		{
			flag = false;
			break;
		}
	}

	return flag;
}

int main()
{
	freopen("D://input.in","r",stdin);
	freopen("D://out.in","w",stdout);		
	
	bool flag;

	cin>>t;

	for(int k=0;k<t;k++)
	{
		flag = true;

		cin>>n; cin>>m;

		for(int i=0;i<n;i++) 
			for(int j=0;j<m;j++) 
					 cin>>x[i][j];

		for(int i=0;i<n;i++) 
		{
			if(!flag) break;
			
			for(int j=0;j<m;j++) 
			{
				if(!IsPossible(i,j))
				{
					flag = false;
					break;
				}
			}
		}

		if(flag) cout<<"Case #"<<k+1<<": YES\n";
		else cout<<"Case #"<<k+1<<": NO\n";

	}

	//printf("\n");
	return 0;
} 

