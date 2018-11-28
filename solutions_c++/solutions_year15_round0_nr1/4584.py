#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
using namespace std;
int main() {
	int a,b,c,t,i,j;
	ifstream cinn("A-large.in");
	ofstream coutt("txt.in");
	string g;
	cinn>>t;
	for(i=0;i<t;i++) {
		a=b=0;
		cinn>>c>>g;
		for(j=0;j<=c;j++) {
			if(a<j) {
				b+=j-a;
				a=j;
			}
			a+=g[j]-'0';
		}
		coutt<<"Case #"<<i+1<<": "<<b<<endl;
	}
}
