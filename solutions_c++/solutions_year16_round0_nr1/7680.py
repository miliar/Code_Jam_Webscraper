//============================================================================
// Name        : codejam2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream oku("A-large.in",ios::in);
	ofstream yaz("cikti.out",ios::out);
	int i,t=0,T,N,ar[11],cnt;
	long top,yed;
	oku>>T;
	while(++t<=T) {
		oku>>N;
		for(i=0;i<10;i++) ar[i]=0;
		cnt=0;
		for(i=1,top=N;i<=10000;i++,top+=N) {
			for(yed=top;yed;yed/=10) {
				if(ar[yed%10]==0) {
					ar[yed%10]=1;
					cnt++;
				}
			}
			if(cnt==10) {
				yaz<<"Case #"<<t<<": "<<top<<endl;
				break;
			}

		}
		if(i==10001) {
			yaz<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
		}
	}
	return 0;
}
