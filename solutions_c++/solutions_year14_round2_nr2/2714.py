#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int count=0;
		int a,b,k;
		scanf("%d %d %d",&a,&b,&k);
		for(int j=0;j<a;j++){
			for(int l=0;l<b;l++){
				if((j&l)<k){
					count++;
				}
			}
		}
		printf("Case #%d: %d\n",i+1,count);
	}
	return 0;
}
