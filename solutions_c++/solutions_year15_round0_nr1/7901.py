#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
	int t,x;
	FILE* fi=fopen("input1.in","r");
	FILE* fo=fopen("output1.txt","w");
	fscanf(fi,"%d",&t);
	for(int x=1;x<=t;x++){
		int smax;
		char shy[1005];
		fscanf(fi,"%d\n",&smax);
		fscanf(fi,"%s",shy);
		//printf("%s\n",shy);
		int curr=shy[0]-'0';
		int need=0;
		for(int i=1;i<=smax;i++){
			if(curr<i){
				need+=(i-curr);
				curr=i+shy[i]-'0';
			}
			else{
				curr+=shy[i]-'0';
			}
		}
		fprintf(fo,"Case #%d: %d\n",x,need);
	}
}