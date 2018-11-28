#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	for(int i=1; i<=t; i++){
		printf("Case #%d:",i);
		int k, c, s;
		scanf("%d%d%d",&k,&c,&s);
		if(k==s){
			for(int j=1; j<=s; j++) printf(" %d",j);
			printf("\n");
		}
		else if(c==1) printf(" IMPOSSIBLE\n");
		else if(s<(k/2+k&1)) printf(" IMPOSSIBLE\n");
		else{
			for(int j=0; j<(k/2+k&1); j++){
				printf(" %d",min(2*j*k+2*j+2,k*k));
			}
		}
	}
}
			
