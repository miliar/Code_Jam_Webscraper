#include <iostream>
#include<string.h>
#include<math.h>
#include<stdio.h>
using namespace std;

int main() {
	int test,a,b,k;
	cin>>test;
	for(int i=0;i<test;i++){
		int count=0;
		cin>>a>>b>>k;
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
