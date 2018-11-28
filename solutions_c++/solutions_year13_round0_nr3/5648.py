#include <sstream>
#include <iostream>
#include <iomanip>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <vector>
//#include "incl.h"
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
#define ZERO(x) memset(x,0,sizeof(x))

int check_palin(unsigned long int x)
{
	unsigned long int z=0,y=x;
	int i,flag=0;

	//count digits
	for(i=0;x>0;i++)	x/=10;
	x=y;
	for(int tmp=0;tmp<i;tmp++) {z=z*10+y%10;y/=10;}
	for(int j=0;j<i/2;j++)
	{
		if(x%10!=z%10) {flag=1;break;}
		x/=10;y/=10;
	}
	if(flag==1) return 0;
	return 1;
}

int run()
{
	int res=0;
	long double a,b;
	unsigned long int x,y;
	cin>>a>>b;
	x=ceill(sqrt(a));
	y=floor(sqrt(b));
//	cout<<check_palin(11);
	for(int i=x;i<=y;i++)
	{
		if(i>3 && i<=9) continue;
		if(check_palin(i)==1) {res++;}
	}
	//print result
	cout<<res;
	return 0;
}

int main()
{
//	freopen("C.in","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int testcase;
	cin>>testcase;
	REP(case_id,testcase)
	{
		cout<<"Case #"<<case_id+1<<": ";
		run();
		cout<<endl;
		fflush(stdout);
	}
	return 0;
}

