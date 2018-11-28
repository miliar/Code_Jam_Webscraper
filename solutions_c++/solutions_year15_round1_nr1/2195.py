#include<iostream>
#include <stdio.h>

using namespace std;

int main(){
	
int a;
	scanf("%d",&a);
	for(int k=1;k<=a;k++){
		int x;
		scanf("%d",&x);
		int vet[x];
		for(int i=0;i<x;i++){
			scanf("%d",&vet[i]);		  
		}
		int a1=0,a2=0,maximo=0;
		for(int i=1;i<x;i++){
			if(vet[i]-vet[i-1]<0){
				a1+=(vet[i-1]-vet[i]);
			}
			maximo=max(maximo,vet[i-1]-vet[i]);
		}
		for(int i=0;i<x-1;i++){
			if(vet[i]>=maximo)
				a2+=maximo;
				else 
					a2+=vet[i];
		}
	printf("Case #%d: %d %d\n",k,a1,a2);
	}
return 0;
}