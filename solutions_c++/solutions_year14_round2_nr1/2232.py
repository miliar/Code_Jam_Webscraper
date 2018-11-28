#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

string A[101];
int N;

int compute() {
  int a=0;
	int total=0;
	int B[101][101];
	int c[101];
	for( int i=0; i<101; i++) {
	  c[i]=0;
		for( int j=0; j<101; j++) {
		  B[i][j] = 0;
		}
	}
	int counter=0;
	for( int i=0; i<N; i++) {
	  counter+=A[i].length();
	}
	for(int i=0; i<100; i++) {
		char temp = A[0][c[0]];
		//cout<<"temp"<<temp<<" ";
		total = 0;
		for(int j=0; j<N; j++) {
			//cout<<A[j][c[j]]<<" ";
			if(A[j][c[j]]!=temp) {
			return -1;
			}
			while(c[j]!=A[j].length()-1 && A[j][c[j]]==A[j][c[j]+1]) {
				c[j]++;
				B[i][j]++;
				total++;
			}
			c[j]++;
			B[i][j]++;
			total++;
			//cout<<A[j][c[j]]<<endl;
		}
		int avg = total/N;
		for( int j=0; j<N; j++) {
		  a+=abs(B[i][j]-avg);
		}
		//cout<<a<<endl;
		counter-=total;
		if(counter==0) break;
	}
	return a;
}

int main() {
  ifstream fin("A.in");
	ofstream fout("A.out");
	int t;
	fin>>t;
	for( int tt=0; tt<t; tt++) {
		bool flag = true;
		fin>>N;
		for( int i=0; i<N; i++) {
		  fin>>A[i];
		}
				int count = compute();
				if(count==-1) {
				  flag = false;
				}
				//cout<<count<<endl;
		if(flag)
			fout<<"Case #"<<tt+1<<": "<<count<<endl;
		else {
			fout<<"Case #"<<tt+1<<": "<<"Fegla Won"<<endl;
		}
	}
}