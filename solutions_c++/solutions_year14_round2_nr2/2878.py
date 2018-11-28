#include<iostream>
using namespace std;
int main(void){
	FILE *f1=fopen("B-small-attempt0.in","r");
	FILE *f2=fopen("output.txt","w");
	int a,b,k;
	int i,j,t,tt;
	int count=0;

	fscanf(f1,"%d",&t);
	tt=1;
	while(tt<=t){
	fscanf(f1,"%d %d %d",&a,&b,&k);
	count=0;
	for(i=0;i<a;i++){
		for(j=0;j<b;j++){
			if( (i&j) < k){
				count++;
			}
		}
	}
	fprintf(f2,"Case #%d: %d\n",tt,count);
	tt++;
	}
}