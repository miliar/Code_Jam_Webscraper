#include <bits/stdc++.h>

using namespace std;

int t;
long long c,d,v;
long long ans,sum,cur;
long long arr[128];

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		scanf("%lld%lld%lld",&c,&d,&v);
		for (int i=0; i<d; i++){
			scanf("%lld",&arr[i]);
		}
		sum = 0;
		cur = 0;
		ans = 0;
		for (int i=0; i<d; i++){
			while (sum < arr[i]-1){
				ans++;
				sum += (c*(sum+1));
			}
			sum += (arr[i]*c);
		}
		while (sum < v){
			ans++;
			sum += (c*(sum+1));
		}
		printf("Case #%d: %lld\n",jj,ans);
	}
	return 0;
}