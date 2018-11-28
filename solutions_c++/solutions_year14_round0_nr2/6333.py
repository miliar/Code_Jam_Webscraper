#include <cstdlib>
#include <stdio.h>
#include <cstring>
#include <complex>
#include <vector>
#include <cmath>
#include <ctime>
#include <iostream>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <iomanip>
#include <utility>
#include <locale>
#include <sstream>
#include <string> // this should be already included in <sstream>
#define FOR(i,n) for(i=0;i<n;i++)
#define FORI(i,a,n) for(i=a;i<=n;i++)
#define FORC(it,C) for(it=C.begin();it!=C.end();it++)
#define scanI(x) scanf("%d",&x)
#define scanD(x) scanf("%lf",&x)
#define print(x) printf("%d\n",x)
#define mod 10000
#define ll unsigned long long
#define max 100000000
#define sq(x) (x*x)
///cout<<(double)(clock() - tStart)/CLOCKS_PER_SEC<<endl;
///clock_t tStart = clock();
#define MAX 1000000
#define  S sqrt(MAX)
#define rP(n) (sieve[n>>6]|=(1<<((n>>1)&31))) 
#define gP(n) sieve[n>>6]&(1<<((n>>1)&31))
#define ct_prime 78498 
typedef long long int lint;


using namespace std;

int main()
{
	int t;
	double c,f,x;
	long double t1,t2,ans,prev,prev1;
	double r=2.0;
	int i;
	cin>>t;
	int in=0;
	while(t--)
	{
		in++;
		t1=t2=ans=prev=prev1=0.0;
		r=2.0;
		cin>>c>>f>>x;
		t1=c/r;
		t2=x/r;
		i=0;
		prev=t1;
		prev1=t2;
		while(1)
		{
			
			i++;
			r+=f;
			ans=prev+x/r;
			t2=x/r+t1;
			if(t2>prev1) break;
			t1+=c/r;
			//cout<<"debug"<<" "<<t1<<" "<<t2<<endl;
			//cout<<"debug1"<<" "<<prev<<" "<<ans<<endl;
			prev=t1;
			prev1=t2;
		//	cout<<prev+x/r<<" "<<prev<<" "<<t1<<" "<<t2<<endl;
			
			
			
		}
	printf("Case #%d: %.7LF\n",in,prev1);
	}
	return 0;
}

