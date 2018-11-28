#include<bits/stdc++.h>
using namespace std;

char str[200]; int mark[200];

int main(){
	
	freopen("input.txt", "r" , stdin);
	freopen ("output.txt","w",stdout);
	
	int t,r,i,j,n;
	scanf("%d",&t);
	
	for(r=1;r<=t;++r){
		scanf("%s",str);
		printf("Case #%d: ",r);
		n=strlen(str);
		char ref=str[0]; int count=1; int z=0;
		char refresh=ref;
		for(i=1;i<n;++i){
			if(str[i]==ref){
				++count;
			}
			else{
				mark[z]=count; ++z;
				count=1; ref=str[i];
			}
		}
		mark[z]=count; ++z;
		if(refresh=='+'){
			if(z%2==0){
				printf("%d\n",z);
			}
			else{
				printf("%d\n",(z-1));
			}
		}
		else{
			if(z%2==0){
				printf("%d\n",(z-1));
			}
			else{
				printf("%d\n",z);
			}
		}
	}
	
	fclose(stdout);
	return 0;
}
