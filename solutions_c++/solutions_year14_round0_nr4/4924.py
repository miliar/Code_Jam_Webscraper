#include<stdio.h>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>

using namespace std;

double a[1002],b[1002];
bool f_cmp(double a,double b){
	return ((b-a)>(double)0);
}

int main(){
	int n,t,cnt1,cnt2,c;
	int psa,pea,psb,peb;
	cin >> t;
	c=t;
	while(t--){
		scanf("%d",&n);
		for(int i=0;i<n;i++) cin >> a[i];
		for(int i=0;i<n;i++) cin >> b[i];

		sort(a,a+n,f_cmp);
		sort(b,b+n,f_cmp);

		psb=0;peb=n-1;
		cnt1=0;cnt2=0;
		//psb=0;peb=n-1;

		//for(int i=0;i<n;i++) printf("%f %f\n",a[i],b[i]);


		for(int i=0;i<n;i++){
			if(a[i]>b[psb]){
				psb++;
				cnt1++;
			}
			else{
				peb--;
			}
			if(psb>peb) break;
		}
		int j,k;
		for(int i=n-1;i>=0;i--){
			j=0;
			while(a[i]>b[j] && j<n){
				j++;
			}
			if(j==n) {
				for(k=0;k<n;k++) if(b[k]!=-1) break;
				b[k]=-1;
				cnt2++;
			}
			else b[j]=-1;
		}

		printf("Case #%d: %d %d\n",c-t,cnt1,cnt2);
	}
	return 0;
}







