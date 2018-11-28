#include<bits/stdc++.h>
using namespace std;
int main(){
	char s[100];
	int len,i,j,k,t,c;
	FILE *ip, *op;
	ip=fopen("B-large.in","r");
	if(ip==NULL){
		printf("error");
		exit(0);
	}
	op=fopen("output.txt","w");
	if(op==NULL){
		printf("error");
		exit(0);
	}
	fscanf(ip,"%d",&t);
	for(i=1;i<=t;i++){
		c=0;
		fscanf(ip,"%s",s);
		len=strlen(s);
		for(j=len-1;j>=0;j--){
		if(s[j]=='-'){
			for(k=0;k<=j;k++){
			if(s[k]=='+'){
				s[k]='-';
			}
			else{
				s[k]='+';
			}
		}
		c++;
		}
	}
	fprintf(op,"Case #%d: %d\n",i,c);
	}
return 0;
}
