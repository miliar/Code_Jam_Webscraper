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
	int i,j,k;
	cin>>t;
	int li=0;
	while(t--)
	{
		li++;
		int A[4][4];
		int B[4][4];
		int a1,a2;
		int count=0;
		cin>>a1;
		FOR(i,4)
		{
			FOR(j,4)
			{
				cin>>A[i][j];
			}
		}
		cin>>a2;
		FOR(i,4)
		{
			FOR(j,4)
			{
				cin>>B[i][j];
			}
		}
		a1--;
		a2--;
		int ans[4];
		int in=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(A[a1][i]==B[a2][j])
				{
					count++;
					ans[in++]=A[a1][i];
				}
			}
		}
		
		if(count==0)
		{
			cout<<"Case #"<<li<<": Volunteer cheated!"<<endl;
		}
		
		else if(count>1)
		{
			cout<<"Case #"<<li<<": Bad magician!"<<endl;
		}
		
		else if(count==1)
		{
			cout<<"Case #"<<li<<": "<<ans[0]<<endl;
		}
	}
	return 0;
}
