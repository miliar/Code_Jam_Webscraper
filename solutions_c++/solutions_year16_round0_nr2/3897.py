#include<cstdio>
#include<fstream>
#include<cstring>
#include<iostream>
using namespace std;
int T,N,S;
string stack;
int main(){
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("B-large.out");
	
	fin>>T;
	
	for(int i=0;i<T;++i){
		N=0;
		fin>>stack;
		S=stack.length();
		for(int k=0;k<S;++k) printf("%c",stack[k]);
		printf("\n");
		for(int j=0;j<S-1;++j){
			if(stack[j]!=stack[j+1]) N++;
		}
		if(stack[S-1]=='-') N++;
		fout<<"Case #"<<(i+1)<<": "<<N<<endl;
	}
	
	fin.close();
	fout.close();
	system("PAUSE");
	return 0;
	
}
