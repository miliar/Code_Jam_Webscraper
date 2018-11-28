#include<bits/stdc++.h>
using namespace std;
int main(){
	long long int n,x,I,J,k,b;
	int sum,t,a[10];
	FILE *input, *output;
	input=fopen("A-large.in","r");
	if(input==NULL){
		printf("ERROR");
		exit(0);
	}
	output=fopen("output.txt","w");
	if(output==NULL){
		printf("ERROR");
		exit(0);
	}
	fscanf(input,"%lld",&t);
	for(I=1;I<=t;I++){
		sum=0;
		fscanf(input,"%lld",&n);
		for(J=0;J<10;J++) a[J]=0;
		if(n==0) fprintf(output,"Case #%lld: INSOMNIA\n",I);
		else{
			for(J=1;;J++){
				x=n*J;
				while(x!=0){
					int dig=x%10;
					if(a[dig]==0){
						a[dig]=1;
						sum+=dig;
					}
					x=x/10;
				}
				if(sum==45 && a[0]==1){
					fprintf(output,"Case #%lld: %lld\n",I,n*J);
					break;
				}
			}
		}
	}
	return 0;
}
