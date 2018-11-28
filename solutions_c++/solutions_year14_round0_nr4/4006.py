#include<iostream>
#include<stdio.h>
#include<fstream>
#include<algorithm>
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
double a[1002],a0[1002];
double b[1002],b0[1002];
int N;

int f(double *a,double *b,int N){
	int n;
		int al,ar,bl,br;
		al=0;ar=N;
		bl=0;br=N;
		n=0;
		int j;
		for(int i=0;i<N;i++){
			if(a[ar-1-i]>b[br-1]){
				n++;
				bl++;
				continue;
			}
			for(j=br-1;j>=bl&&b[j]>a[ar-1-i];j--);
			for(;j>=bl;j--){
				b[j+1]=b[j];
			}
			bl++;
		}
		return n;
}

int main(){
	int CaseNum;
	int i,j;
	ifstream in;
	ofstream out;
	//in.open("test.txt");
	in.open("D-large.in");
	out.open("out.txt");
	in>>CaseNum;
	for(int Case=0;Case<CaseNum;Case++){
		in>>N;
		for(int i=0;i<N;i++)in>>a[i];
		for(int i=0;i<N;i++)in>>b[i];
		
		sort(a,a+N);
		sort(b,b+N);

		for(int i=0;i<N;i++){
			a0[i]=a[i];
			b0[i]=b[i];
		}

		int n=f(a,b,N);

		for(i=0;i<N;i++){
			a[i]=a0[i];
			b[i]=b0[i];
		}

		int m=0,t;
		for(i=0,j=0;i<N;i++){
			if(a[i]>b[j]){
				j++;
				m++;
			}
		}



		out<<"Case #"<<Case+1<<": "<<m<<" "<<n<<endl;
	}
	return 0;
}