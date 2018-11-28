/*
ID: Tariqul
PROG: 
LANG: C++
*/

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

char BUFFER[100000 + 5];
bool readn(int &n)	{ return scanf("%d",&n) == 1; } 
bool readl(Long &n)	{ return scanf("%I64d",&n) == 1; } 
bool readd(double &n){ return scanf("%lf",&n) == 1; } 
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }


/*int play1(set<double> st1, set<double> st2)
{		
	set<double>::iterator p;
	while(sz(st1))
	{
		p = st2.end(); p--;
		if(*(st1.begin()) < *(p))
		{
			st1.erase(st1.begin());
			st2.erase(p); 
			continue;
		}
		return sz(st1);		
	}
	return 0;
}
*/

int play2(set<double> st1, set<double> st2)
{
	double n;
	set<double>::iterator p;
	while(sz(st1))
	{
		n = *st1.begin();
		p = st2.lower_bound(n); 
		if(p == st2.end())return sz(st1);
		st1.erase(st1.begin());
		st2.erase(p); 			
	}
	return 0;	
}

set<double> st1,st2;

void doit()
{
	int i,n; double m; readn(n); st1.clear(); st2.clear();
	fo(i,0,n){ readd(m); st1.insert(m); }
	fo(i,0,n){ readd(m); st2.insert(m); }
	cout << (n - play2(st2,st1));	
	cout << " ";
	cout << play2(st1,st2);	
}

int main()
{
	freopen("D://input.txt","r",stdin);
	freopen("D://output.txt","w",stdout);
	int Case,t;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{		
		printf("Case #%d: ",Case);
		doit(); 
		cout << endl;
	}
	return 0;
} 

