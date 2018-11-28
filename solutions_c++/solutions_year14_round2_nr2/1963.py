#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<stdint.h>
#include<stdlib.h>
#include<climits>
#include<stdio.h>
#include<cmath>
#include<queue>
#include<vector>
#include<map>
using namespace std;
int main(){
	int a,b,k,t;
	
	scanf("%d",&t);
	
	for(int ie = 1;ie<=t;ie++){
		
		scanf("%d%d%d",&a,&b,&k);
		int c = 0;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				if((i&j) < k){
					++c;
				}
			}
		}
		printf("Case #%d: %d\n",ie,c);
	}
	
	return 0;
}

