#include<stdio.h>
#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
double arr1[1000],arr2[1000];
int main(){
int i,j,t,n,k,c,d;
scanf("%d",&t);
for(k=1;k<=t;k++){
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%lf",&arr1[i]);
	}
	for(i=0;i<n;i++){
		scanf("%lf",&arr2[i]);
	}
	sort(arr1,arr1+n);
	sort(arr2,arr2+n);
	//for(i=0;i<n;i++)printf("%.3f ",arr[i]);printf("\n");
	//for(i=0;i<n;i++)printf("%.3f ",arr2[i]);printf("\n");
	c=d=0;
	j=0;	
	for(i=0;i<n;i++){
		while(j<n&&arr1[j]<arr2[i])j++;
		if(j<n)c++;
		else break;
		j++;
	}
	j=0;
	for(i=0;i<n;i++){
		while(j<n&&arr1[i]>arr2[j])j++;
		if(j<n)d++;
		else break;	
		j++;
	}
	printf("Case #%d: %d %d\n",k,c,n-d);
}
return 0;
}


		
	






