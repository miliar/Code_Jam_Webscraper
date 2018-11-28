#include<stdio.h>
#include<algorithm>
using namespace std;
int n;
double vol,temp;
double v[111],t[111];
int main(){
	int _,T;
	scanf("%d",&_);
	for(int T=1; T<=_; T++){
		scanf("%d%lf%lf",&n,&vol,&temp);
//		printf("%d %lf %lf\n",n,vol,temp);
		double lef = 0, rig = 1e9, small = 1e9, large = 0;
		for(int i=1; i<=n; i++){
			scanf("%lf%lf",&v[i],&t[i]);
//			printf("%lf %lf\n",v[i],t[i]);
			small = min(small,t[i]);
			large = max(large,t[i]);
			lef += v[i];
			rig = min(rig, v[i]);
		}
		lef = vol / lef;
		rig = vol / rig;

		for(int i=1; i<=n; i++)
			for(int j=i+1; j<=n; j++)
				if(t[j] < t[i]){
					swap(t[i],t[j]);
					swap(v[i],v[j]);
				}

		printf("Case #%d: ",T);
		if(temp < small || temp > large){
			puts("IMPOSSIBLE");
			continue;
		}
		if(temp == small || temp == large){
			double v2 = 0;
			for(int i=1; i<=n; i++)
				if(t[i] == temp)
					v2+=v[i];
			printf("%.10lf\n",vol/v2);
			continue;
		}
		for(int run=0; run<120; run++){
			double mid = (lef + rig)/2;
			double tot = vol;
			small=0;
			for(int i=1; i<=n; i++){
				if(tot >= v[i] * mid){
					tot-=v[i]*mid;
					small+=v[i]*mid*t[i];
				}else{
					small+=tot*t[i];
					break;
				}
			}
			small/=vol;

			tot=vol;
			large=0;
			for(int i=n; i>=1; i--){
				if(tot >= v[i] * mid){
					tot-=v[i]*mid;
					large+=v[i]*mid*t[i];
				}else{
					large+=tot*t[i];
					break;
				}
			}
			large/=vol;
			if(temp < small || temp > large)
				lef = mid;
			else
				rig = mid;

		}
		printf("%.10lf\n",(lef+rig)/2);
	}
	return 0;
}
