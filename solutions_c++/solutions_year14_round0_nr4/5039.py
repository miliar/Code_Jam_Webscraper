#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;


int main ()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	float arr[10001],arr1[10001];
	int t,i;
cin >>t;
	int t1 =0;
	while (t1 <t ){
	     int sum = 0;
		int num;
		cin >> num;
		for(i = 0; i < num ;i++) {
		cin>>arr[i];
		}
		for(i = 0; i < num ;i++) {
		cin>>arr1[i];
		}
	     sort(arr, arr+ num);
	     sort(arr1,arr1+num);
	     
	      int  j = 0;
	     for(i = 0; i<num;i++) {
	     	if(arr[i] > arr1[j]) {
	     		sum++;
	     		j++;
	     	}
	     	
	     	
	     	
	     }
	     int sub  = 0;
	     int kk1 = 0;
	     
	     
	     int sum1 = 0;
	     for(i =num-1;i>= 0;i--) {
	     	sum1 = 0;
	     	for(j= 0;j<num;j++){
	     		if(arr[i] > arr1[j]) {
	     			sum1++;
	     		
	     		}
	     		else {
	     			break;
	     		}
	     	}
	     	if(sum1 == num){
	     		sub++;
	     		arr1[kk1] = -10;
	     		kk1++;
	     	}
	     	
	     	else{
	     		arr1[j] = -10;
	     	} 
	     }
	     printf("Case #%d: %d %d\n",t1+1,sum,sub);
	     t1++;
	     
		
	}
	
	return 0;
}
