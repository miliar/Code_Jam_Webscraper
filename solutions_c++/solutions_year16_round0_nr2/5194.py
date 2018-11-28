#include<bits/stdc++.h>
using namespace std;
int main(){
	char s[100];
	int l,i,j,k,t,count;
	FILE *input, *output;
	input=fopen("B-large.in","r");
	if(input==NULL){
		printf("ERROR");
		exit(0);
	}
	output=fopen("output.txt","w");
	if(output==NULL){
		printf("ERROR");
		exit(0);
	}
	fscanf(input,"%d",&t);
	for(k=1;k<=t;k++){
		fscanf(input,"%s",s);
		count=0;
		l=strlen(s);
		for(i=l-1;i>=0;i--){
			if(s[i]=='-'){
				for(j=0;j<=i;j++){
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
				count++;
			}
		}
	fprintf(output,"Case #%d: %d\n",k,count);
	}
return 0;
}
