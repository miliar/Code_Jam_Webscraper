#include <cstdio>
#include <queue>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <utility>
#define pii pair<int, int>
#define VI vector < int >
#define PB push_back
#define FOR(i,a,b) for(i=a;i<b;i++)
#define FORD(i,a,b) for(i=a;i>b;i--)
typedef long long LL;
using namespace std;
int main()
{
	int i,j,k,n,t;
	double c,f,x;
	cin>>t;
	double ans=0.0;
	for(k=1;k<=t;k++)
	{
		cin>>c>>f>>x;
		cout<<"Case #"<<k<<": ";
		ans=0.0;
		double dd=0;
		double rate=2;
		//int time=0;
		if(x<=c)
		{	
			//cout<<x/2<<endl;
			printf("%.7lf\n",x/2.0);
		}
		else
		{
			while(1)
			{
				if((x-c)/rate > (x)/(rate+f))
				{
					ans+=c/rate;
					rate+=f;
				}
				else
				{
					ans+=x/rate;
					break;
				}
			}
			printf("%.7lf\n",ans);
		}
	}
	return 0;
}
