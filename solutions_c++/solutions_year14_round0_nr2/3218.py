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
#define eps 1e-6

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

void doit()
{
	double C,F,X,t = 0,t1,t2,t3,cf = 2;
	//int cnt = 100;
	readd(C); readd(F); readd(X);
	//mi = X / cf;
	while(1)
	{
		t1 = X / cf; t2 = X / (cf + F); t3 = C / cf;
		/*if( (( X + eps ) < cf) && (( C + eps ) < cf))
		{
			if(cnt == 0)break; cnt--;
		}*/
		if((t2 + t3) < t1){ cf += F; t += t3; continue; }	
		//mi = min(mi,t + t1); t += t3; cf += F;
		t += t1; break;
	}
	printf("%.7lf",t);
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

