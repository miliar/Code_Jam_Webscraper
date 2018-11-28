#include<iostream>
#include<fstream>
using namespace std;



int main(){
	FILE *f1,*f2;
	f1=fopen("input.txt","r");
	f2=fopen("output.txt","w");
	int t;
	fscanf(f1,"%d",&t);
	for(int i=1;i<=t;i++){
		int n, arr[1001];
		fscanf(f1,"%d ",&n);
		for(int j=0;j<=n;j++){
			char c;
			fscanf(f1,"%c",&c);
			int num=c-'0';
			arr[j]=num;
		}
		int sum=0, answer=0;
		for(int j=0;j<=n;j++){
			if(sum<j){answer+=(j-sum);sum+=(j-sum);}
			sum+=arr[j];
		}
		fprintf(f2,"Case #%d: %d\n",i,answer);
	}
	return 0;
}