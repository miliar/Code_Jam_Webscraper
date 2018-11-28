#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;


int main ()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	float a[1001],a1[1001];int count = 0;
	int t,i;
	scanf("%d",&t);
	int x1 =0;
	while (x1 <t ){
		count =0;
		int n;
		scanf("%d",&n);
		for(i = 0; i < n ;i++) {
			scanf("%f",&a[i]);
		}
		for(i = 0; i < n ;i++) {
			scanf("%f",&a1[i]);
		}
	     sort(a, a+ n);
	     sort(a1,a1+n);
	     
	    int  j = 0;
	     for(i = 0; i<n;i++) {
	     	if(a[i] > a1[j]) {
	     		count++;
	     		j++;
	     	}
	     	
	     	
	     	
	     }
	     int s  =0;
	     int k1 =0;
	     int k2 =n-1;
	     
	     int count1 = 0;
	     for(i =n-1;i>= 0;i--) {
	     	count1 = 0;
	     	for(j= 0;j<n;j++){
	     		if(a[i] > a1[j]) {
	     			count1++;
	     		
	     		}
	     		else {
	     			break;
	     		}
	     	}
	     	if(count1 == n){
	     		s++;
	     		a1[k1] = 0;
	     		k1++;
	     	}
	     	
	     	else{
	     		a1[j] = 0;
	     	} 
	     }
	     printf("Case #%d: %d %d\n",x1+1,count,s);
	     x1++;
	     
		
	}
	
	return 0;
}
