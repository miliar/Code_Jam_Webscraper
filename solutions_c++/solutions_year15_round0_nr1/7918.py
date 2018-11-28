#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;


int main(){
	freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
	int t;
	scanf("%d", &t);
	for (int tc=1; tc<=t; tc++){
		int sm,c=0;
		char a[1004];
		scanf("%d",&sm);
		for (int i=0; i<=sm; i++){
			scanf("%c",&a[i]);
			if (a[i]==32)
				i--;
		}		int sum;
		for (int i=0; i<=sm;i++){
			sum=0;
			if(a[i]=='0'){
				
				for (int j=0; j<i; j++){
					sum=sum+a[j]-48;	
				}
				if ((sum+c)>i){
					c--;
					sum=sum-i;
				}
				c++;
			}
		}
		printf("Case #%d: %d\n",tc,c);
	}
}