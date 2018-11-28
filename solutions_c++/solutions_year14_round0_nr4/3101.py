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
#include <iomanip>

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
    
	int t,n,cnt1=0,cnt2=0;
	double in;
	   
    cin>>t;
    
    for(int k=1; k<=t;k++)
	{  
		vector<double> v1, tmp1;
		vector<double> v2, tmp2;

		cin>>n;
		for(int i=0;i<n;i++) {cin>>in;v1.push_back(in);}
		for(int i=0;i<n;i++) {cin>>in;v2.push_back(in);}
		
		sort(v1.begin(),v1.end()); sort(v2.begin(),v2.end());
		tmp1=v1; tmp2=v2;

		cnt1=n;
		for (std::vector<double>::iterator it1 = tmp1.begin(); it1 != tmp1.end(); ++it1)
		{
			for (std::vector<double>::iterator it2 = tmp2.begin(); it2 != tmp2.end(); ++it2)
			{
				if(*it1<*it2){cnt1--;*it2=0;break;}
			}
		}

		tmp2=v2;
		cnt2=n;
		for (std::vector<double>::iterator it1 = tmp2.begin(); it1 != tmp2.end(); ++it1)
		{
			for (std::vector<double>::iterator it2 = tmp1.begin(); it2 != tmp1.end(); ++it2)
			{
				if(*it1<*it2){cnt2--;*it2=0;break;}
			}
		}
		
		cout<<"Case #"<<k<<": "<< (n-cnt2)<<" "<<cnt1;
		printf("\n");
	}
   
    return 0;
}