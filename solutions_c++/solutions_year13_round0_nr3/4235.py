//
//  problemC.cpp
//  codeJam_QualificationRound
//
//  Created by Jereneal Kim on 13. 4. 14..
//  Copyright (c) 2013년 Jereneal Kim. All rights reserved.
//

#include <iostream>
using namespace std;

int isPalindrome(__int64_t val)
{
	__int64_t tmp=val;
	int arr[1001]={0},i,k;
	for(i=0;tmp>0;i++){
		arr[i]=tmp%10;
		tmp/=10;
	}
	k=i-1;
	for(i=0;i<=k;i++){
		if(arr[i]==arr[k-i]){
			
		}else{
			return 0;
		}
	}
	return 1;
}


int main(int argc, const char **argv)
{
	FILE *fp,*inp;
	int k=0,t,count=0;
	__int64_t i,j,n,m;
	__int64_t arr[1001]={0};
	fp=fopen(argv[1],"w");
	inp=fopen(argv[2],"r");
	
	
	for(i=1;i<10000000;i++){
		if(isPalindrome(i)&&isPalindrome(i*i)){
			arr[k]=i;
			k++;
		}
	}
	
	fscanf(inp,"%d",&t);
//	scanf("%d",&t);
	
	for(i=1;i<=t;i++){
		fscanf(inp, "%lld %lld",&n,&m);
//		scanf("%lld %lld",&n,&m);
		count=0;
		j=0;
		while(1){
		
			if(n<=arr[j]*arr[j]&&arr[j]*arr[j]<=m){
				count++;
			}
			if(arr[j]*arr[j]>m||arr[j]==0){
				break;
			}
			j++;
		}
		
		
		fprintf(fp,"Case #%lld: %d\n",i,count);
		printf("Case #%lld: %d\n",i,count);
		
	}
	
	return 0;
}
