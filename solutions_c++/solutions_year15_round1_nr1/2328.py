#include<iostream>
#include<cstdio>

int main(){
	int test_cases,N,M,maxdiff =0;
	long long int count1=0,count2=0;
	scanf("%d",&test_cases);
	for(int t = 0;t<test_cases;t++){
		scanf("%d",&N);
		int arr[N];
		maxdiff = 0;
		count1=0;
		count2=0;
		scanf("%d",&arr[0]);
		for(int i=1;i<N;i++){
			scanf("%d",&arr[i]);
			if(arr[i-1] > arr[i]){
				count1 += (arr[i-1] - arr[i]);
				if(maxdiff < (arr[i-1] - arr[i])){
					maxdiff = arr[i-1] - arr[i];
				}
			}
		}
		for(int i=0;i< (N-1); i++){
			if(arr[i] <= maxdiff){
				count2 += arr[i];
			}
			else{
				count2 += maxdiff;
			}
			
		}
		printf("Case #%d: %lld %lld\n",t+1,count1,count2);
	}
}
