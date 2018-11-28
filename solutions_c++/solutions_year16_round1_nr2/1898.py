#include <iostream>
#include <list>
#include <vector>
#include<cstring>
#include<fstream>
using namespace std;


int main() {
	// your code goes here
	ofstream out;
	out.open("2b.out");
	ifstream in;
	in.open("2b.in");
	int t,i,num[2501];
	in>>t;
	for(int r=1;r<=t;r++){
		memset(num,0,sizeof(num));
		int n,nm,j;
		in>>n;
		for(i=0;i<2*n-1;i++){
			for(j=0;j<n;j++){
				in>>nm;
				num[nm]++;
			}
		}
		out<<"Case #"<<r<<":";
		for(i=1;i<=2500;i++){
			if(num[i]%2){
				out<<" "<<i;
			}
		}
		out<<"\n";
	}
	return 0;
}
