#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main(){
	int T,frd,Smax;
	char *aud=new char[1001];
	FILE* fp1;
	FILE* fp2;
	fp1=fopen("input.in","rt+");
	fp2=fopen("output.in","wt+");
	fscanf(fp1,"%d",&T);
	for(int i=0;i<T;i++){
		frd=0;
		int sum=0;
		fscanf(fp1,"%d",&Smax);
		fscanf(fp1,"%s",aud);
		for(int k=0;k<Smax+1;k++){
			if(sum<k){
				frd+=k-sum;
				sum+=k-sum;
			}
			sum+=int(aud[k])-48;
		}
		fprintf(fp2,"Case #%d: %d\n",i+1,frd);
	}


	return 0;
}