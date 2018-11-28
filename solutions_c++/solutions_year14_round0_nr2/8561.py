#include <bits/stdc++.h>
using namespace std;
#define SZ(V) (long long )V.size()
#define ALL(V) V.begin(), V.end()
#define RALL(V) V.rbegin(), V.rend()
#define FORN(i, n) for(i = 0; i < n; i++)
#define FORAB(i, a, b) for(i = a; i <= b; i++)
#define PB push_back  
#define MP make_pair
#define MOD 1000000007LL
#define no_of_tags 3

typedef pair<int,int> PII;
typedef pair<double, double> PDD;
typedef long long LL;

int main()
{
	LL t,test,i;
	double rate=2.0,c,f,x,total_time=0.0,time1=0.0,level_complete;
	cin >> t;
	FORAB(test,1,t)
	{
		total_time=0.0;
		rate=2.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		while(1){
			time1=c/rate;
			level_complete=x/rate;
			if(level_complete<=time1+x/(rate+f))
			{
				total_time+=level_complete;
				break;
			}
			total_time+=time1;
			rate+=f;
		}
		printf("Case #%lld: %.7lf\n",test,total_time);
	}
	return 0;
}