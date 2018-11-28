#include<iostream>
#include<fstream>
#include<string.h>

using namespace std;

int parseInt(char c){
	switch(c){
		case '0':return 0;
		case '1': return 1;
		case '2': return 2;
		case '3': return 3;
		case '4': return 4;
		case '5': return 5;
		case '6': return 6;
		case '7': return 7;
		case '8': return 8;
		case '9': return 9;
	}
}

int main(){
	ifstream ifile("A-small-attempt0.in");
	ofstream ofile("output.txt");
	int i,T,S,counter,sum,cases=1,arr2[100000],k,length,flag=0,total=0;;
	char arr[100000];
	ifile>>T;
	while(T--){
		total=0;
		flag=0;
		sum=0;
		counter=0;
		ifile>>S;
		ifile>>arr;
		length=strlen(arr);
		for(i=0;i<length;i++){
			k=parseInt(arr[i]);
			arr2[i]=k;
		}
		for(i=0;i<length;i++){
			sum=0;
			if(arr2[i]>0 && counter<i){
				total+=i-counter;
				sum=total;
				flag=1;
			}
			counter+=arr2[i];
			if(flag==1)
				counter+=sum;
			flag=0;
		}
		ofile<<"Case #"<<cases<<": "<<(total)<<"\n";
		cases++;
	}	
	return 0;
}