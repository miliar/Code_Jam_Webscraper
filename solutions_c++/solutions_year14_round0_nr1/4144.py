#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;

/*
int main(){
	int CaseNum;
	ifstream in;
	ofstream out;
	in.open("test.txt");
	out.open("out.txt");
	in>>CaseNum;
	for(int Case=0;Case<CaseNum;Case++){



	out<<"Case #"<<Case+1<<":";
	}
	return 0;
}
*/


int main(){
	int CaseNum;
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("out.txt");
	in>>CaseNum;
	
	int a1,a2,a;
	int t,r,n;
	int answer[16]={0};
	for(int Case=0;Case<CaseNum;Case++){
		a1=0;
		a2=0;
		in>>r;
		for(int i=1;i<r;i++){
			for(int c=0;c<4;c++)in>>t;
		}
		for(int c=0;c<4;c++){
			in>>t;
			a1|=1<<(t-1);
		}
		for(int i=r+1;i<=4;i++){
			for(int c=0;c<4;c++)in>>t;
		}

		in>>r;
		for(int i=1;i<r;i++){
			for(int c=0;c<4;c++)in>>t;
		}
		for(int c=0;c<4;c++){
			in>>t;
			a2|=1<<(t-1);
		}
		for(int i=r+1;i<=4;i++){
			for(int c=0;c<4;c++)in>>t;
		}

		a=a1&a2;
		n=0;
		for(int i=0;i<16;i++){
			answer[i]=(a>>i)&1;
			n+=answer[i];
			if(answer[i]>0)t=i+1;
		}


		out<<"Case #"<<Case+1<<": ";
		if(n==0)out<<"Volunteer cheated!"<<endl;
		else if(n>1)out<<"Bad magician!"<<endl;
		else out<<t<<endl;
	}
	return 0;
}