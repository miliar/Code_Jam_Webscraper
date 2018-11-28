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

bool IsPalindromNumber(long long number)
{
	long long reverse = 0, temp;
		
	temp = number;
	
	while( temp != 0 ) {
		reverse = reverse * 10;
		reverse = reverse + temp%10;
		temp = temp / 10;
	}
	
	if ( number == reverse ) return true;
	else return false;
}

bool IsPalindromString(string str)
{
	string tmp = str;
	reverse(str.begin(), str.end());
	if(tmp == str) return true;
	else return false;
}

int main()
{
	freopen("D://input.in","r",stdin);
	freopen("D://out.in","w",stdout);	
	
	int t = 0;
	double d;
	long cnt = 0;
	long long A , B;

	cin>>t;

	for(int i=0;i<t;i++)
	{
		cin>>A; cin>>B;

		for(long long j=A;j<=B;j++)
		{
			if(IsPalindromNumber(j))
			{
				d = sqrt((double)j);
				string str;
				stringstream s;
				s << d; s >> str;

				if(count(str.begin(), str.end(),'.') == 0)
				{
					if(IsPalindromString(str)) cnt++;
				}
			}
		}

		cout<<"Case #"<<i+1<<": "<<cnt<<"\n";
		cnt = 0;
	}

	//printf("\n");
	return 0;
} 

