#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
FILE *fi,*fo;
int addtime(int sum, int next){
	int i=0;
	for(;sum>next;i++){
		sum+=(sum-1);
	}
	return i;
}

int main(){
	fi=fopen("A-small-attempt5.in","r");
	fo=fopen("A-small-attempt5.out","w");
	int T;
	fscanf(fi,"%d",&T);
	int z=1;

	while(z<=T){
		int a=0;
		int n=0;
		int sum=0;
		int del=0;
		int add=0;

		fscanf(fi,"%d %d",&a,&n);
		int *arr,*brr;
		arr=(int*)malloc(sizeof(int)*n);
		brr=(int*)malloc(sizeof(int)*n);
		for(int i=0;i<n;i++){
			fscanf(fi,"%d",&arr[i]);

		}
		std::sort(arr,arr+n);
		for(int i=0;i<n;i++){
			brr[i]=arr[i];
		}

		if(a==1){
			fprintf(fo,"Case #%d: %d\n", z, n);
			z++;
			continue;
		}

		int j=0;
		for(;j<n;j++){
			if(a>arr[j]){
				a=a+arr[j];
				brr[j]=0;
			}
			else
				break;
		}
		int asd=0;
		int tr=0;
		while(j<n){
			while(1){
				if(a<=arr[j]){
					a=2*a-1;
					asd++;

				}
				else{
					brr[j]=asd;
					a+=arr[j];
					break;

				}
			}
			j++;
			tr++;
		}
		j--;
		int count =0;
		int answer=0;
		for(int s=j;brr[s]>0;s--){
			count++;
			brr[s]--;
		}
		if (count==0){
			fprintf(fo,"Case #%d: %d\n",z, 0);
			z++;
			continue;
		}
		answer=count;

		int	index=1;
		while(1){
			count =index;
			for(int s=j;brr[s]>0;s--){
				count++;
				brr[s]--;
			}
			index++;

			if(count<answer)
				answer=count;
			if(brr[j]<=0)
				break;

		}
		if(index<answer)
			answer=index;


		fprintf(fo,"Case #%d: %d\n",z, answer);



		free (arr);
		free (brr);

		z++;
	}
}
