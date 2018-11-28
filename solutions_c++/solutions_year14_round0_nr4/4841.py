#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;
main(){
	int i,j,k,n,t,w,flag=1,cnt1,cnt2;;
	double a[1005],b[1005];
	scanf("%d",&t);
	for(w=1;w<=t;w++){
		int mark[1005]={0};
		scanf("%d",&n);
		for(i=0;i<n;i++) 
			scanf("%lf",&a[i]);
		for(i=0;i<n;i++) 
			scanf("%lf",&b[i]);
		sort(a,a+n); 
		sort(b,b+n);
		flag=1;
		for(i=n-1,j=n-1,cnt1=0;j>=0;){
			if(a[i]<b[j]){
				j--;
			}
			else{
				j--; i--; cnt1++;
			}
		}
		cnt2=0;
		for(i=n-1,j=n-1;i>=0;i--){
			if(b[j]>a[i]){
				j--; 
				cnt2++;
			}
		}
		printf("Case #%d: %d %d\n",w,cnt1,n-cnt2);
	}
}
