#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int main(){
	int t,sum_1,sum_2,n,idn,x;
	double data_n[1003],data_k[1003],max_n,max_k;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		sum_1 = sum_2 = 0;
		scanf("%d",&n);
		max_n = max_k = 0;
		for(int i=0;i<n;i++){
			scanf("%lf",&data_n[i]);
		}
		for(int i=0;i<n;i++){
			scanf("%lf",&data_k[i]);
		}
		sort(data_n,data_n+n);
		sort(data_k,data_k+n);
		idn = 0;
		x = 0;
		while(idn<n){
			while(data_n[x]>data_k[idn]){
				idn++;
				sum_2++;
				if(idn==n) goto lolo;
			}
			x++;
			idn++;
		}
		lolo:
		idn = n-1;
		x = n-1;
		while(idn>=0){
			while(data_k[idn]>=data_n[x]){
				idn--;
				sum_1++;
				if(idn==-1) goto lili;
			}
			x--;
			idn--;
		}
		lili:
		
		sum_1 = n - sum_1;
		printf("Case #%d: %d %d\n",tt,sum_1,sum_2);
	}
}
