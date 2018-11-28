#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	FILE *fpo,*fpi;
	char output[10];
	fpo = fopen("output.txt","w");
	fpi = fopen("input.txt","r");

	int t;
	int value,maxshy_level,extra,acc;
	char ch;
	fscanf(fpi,"%d\n",&t);
	//ch = getchar();

	int total = t;
	char str[1002];
	while(t--){
		acc = extra = 0;
		fgets(str, 1002, fpi);
	//	cout<<"Given String :"<<str;
		maxshy_level = str[0] - 0x30;
		for(int i=0;i<= maxshy_level ;i++){
			value = str[i+2] - 0x30;
			acc += value;
			if(acc <= i){
				extra++;
				acc++;
			} 

		}
		sprintf(output,"case #%d: %d\n",total-t,extra);
		cout<<output;
		fprintf(fpo,"%s",output);


	}







}
