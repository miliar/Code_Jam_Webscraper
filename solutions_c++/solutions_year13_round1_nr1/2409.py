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
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define PI 3.141592
int run()
{
	int res=0;
	double r,t;
	unsigned long long int n=0;
	double v;
	cin>>r>>t;
	
	v=t;
//	cout<<v<<" "<<r<<endl;
/*	for(long long int i=(sqrt(v)+100);i>0;i--)
		if(i*i-i > v) n=(i);
		else break;
	*/
	
	n=floor((1-2*r+sqrt((2*r-1)*(2*r-1)+4*2*v))/4);
	//print result
	cout<<n;
	return 0;
}

int main()
{
//	freopen("A.in","r",stdin);
	freopen("A-small-attempt0.in","r",stdin);freopen("A.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
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

