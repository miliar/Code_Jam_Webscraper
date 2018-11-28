//#include "stdafx.h"

#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
//#include <cstdlib> 
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

char BUFFER[100000 + 5];
bool readn(int &n)  { return scanf("%d",&n) == 1; } 
bool readl(Long &n) { return scanf("%I64d",&n) == 1; } 
bool readd(double &n){ return scanf("%lf",&n) == 1; } 
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }

int main()
{
    freopen("F://input.in","r",stdin);
	freopen("F://output.txt","w",stdout);
    
   int t, x, c, a[4], b[4],cnt=0,res;
   
    cin>>t;
    
    for(int k=1; k<=t;k++)
	{  
		cin>>x;

		for(int j=1;j<=4;j++)
		{
			if(x==j){ cin>>a[0];	cin>>a[1];	cin>>a[2];cin>>a[3];}
			else{ cin>>c;	cin>>c;	cin>>c;	cin>>c;	}
		}

		cin>>x;

		for(int j=1;j<=4;j++)
		{
			if(x==j){ cin>>b[0];	cin>>b[1];	cin>>b[2];cin>>b[3];}
			else{ cin>>c;	cin>>c;	cin>>c;	cin>>c;	}
		}

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[i]==b[j]) {cnt++;res=a[i];}
			}
		}

		if(cnt==0)cout<<"Case #"<<k<<": Volunteer cheated!";
		else if(cnt==1)cout<<"Case #"<<k<<": "<<res;
		else if(cnt>1) cout<<"Case #"<<k<<": Bad magician!";

		cnt=0;
		printf("\n");
	}
   
    return 0;
}