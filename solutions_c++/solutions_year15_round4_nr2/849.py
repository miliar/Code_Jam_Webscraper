#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#include <algorithm>
#define eps 1e-14
using namespace std;

int i,j,n,m,k;
double needV,needT;


struct water{
	double rate,temp;
	water(){}
	water(double _rate , double _tmp){
		rate = _rate;
		temp = _tmp;
	}
};
bool operator < (water a , water b){
	return a.temp<b.temp;
}
water a[10000];

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w", stdout);
	int tt;
	cin>>tt;
	for(int ll=1;ll<=tt;ll++){
		cin>>n>>needV>>needT;
		for(i=0;i<n;i++)
			cin>>a[i].rate>>a[i].temp;

		sort(a,a+n);
		double ans = 2000000000;
		double x,l=0,r=1000000000;
		for(int xx = 1;xx<65;xx++){
			x=(l+r)/2;
			double curv=0;
			double mricx=0;

			double suck=0;
			for (i=0;i<n;i++)
				suck+=a[i].rate;
			if(suck*x+1e-12 < needV){
				l=x;
				continue;
			}

			for(i=0;i<n;i++){
				if(curv+a[i].rate*x < needV){
					curv+=a[i].rate*x;
					mricx+=a[i].rate*x*a[i].temp / needV;
				} else
				{
					mricx+=(needV-curv)*a[i].temp / needV;
					curv=needV;
					break;
				}
			}

			

			double mintemp=mricx;


			curv=0;
			mricx=0;
			for(i=n-1;i>=0;i--){
				if(curv+a[i].rate*x < needV){
					curv+=a[i].rate*x;
					mricx+=a[i].rate*x*a[i].temp / needV;
					
				} else{
					mricx+=(needV-curv)*a[i].temp / needV;
					curv=needV;
					break;
				}
			}

			double maxtemp=mricx;
			if(needT>=mintemp -eps && needT<=maxtemp +eps ){
				ans=min(ans , x);
				r=x;
			} else
				l=x;
		}


		cout<<"Case #"<<ll<<": ";
		if (ans > 1000000000)
			cout<<"IMPOSSIBLE"<<endl;
		else
			printf("%.9lf\n",ans);
	}
	return 0;
}
