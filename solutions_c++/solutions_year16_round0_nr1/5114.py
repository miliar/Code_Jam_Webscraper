#include<bits/stdc++.h>
using namespace std;
int main(){
	long long int n,a,i,j,k,flag[10],b;
	int sum,t;
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
	for(j=1;j<=t;j++){
		fscanf(input,"%lld",&n);
		sum=0;
		for(i=0;i<10;i++)
			flag[i]=0;
		if(n==0){
			fprintf(output,"Case #%lld: INSOMNIA\n",j);
		}
		else{
			for(i=1;;i++){
				a=n*i;
				while(a!=0){
					int temp=a%10;
					if(flag[temp]==0){
						flag[temp]=1;
						sum+=1;
					}
					a=a/10;
				}
				if(sum==10){
					fprintf(output,"Case #%lld: %lld\n",j,n*i);
					break;
				}
			}
		}
	}
	return 0;
}
