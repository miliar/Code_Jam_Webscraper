#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

double multiply(int b,int a){
	double arr[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}},sign=1;
	if(a<0){
		sign=-1;
		a=-a;
	}
	if(b<0){
		sign*=-1;
		b=-b;
	}
	return (arr[a-1][b-1])*sign;
}

void find(int tc){
	long long int L=0,X=0,count=0;
	double res=1,find_item[3]={2,3,4};
	int k=0;
	fin>>L>>X;
	char ch[100000];
	fin>>ch;
	for(long long int i=0;i<X;i++){
		for(long long int j=0;j<L;j++){

			res=multiply(int(ch[j])-103,res);
			if(res==find_item[k]){
				if(res!=4){
					k++;
					res=1;
				}
			}
		}
	
	}
	if(res==4 && k==2)
		fout<<"Case #"<<tc<<": YES\n";
	else 
		fout<<"Case #"<<tc<<": NO\n";
}

void main(){
	int tc;
	fin>>tc;
	for(int i=1;i<=tc;i++){
		find(i);
	}
}