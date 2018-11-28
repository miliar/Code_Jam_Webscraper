#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;
//bool a[101];
//void init(){
//	for (i=0; i< 101; i++)
//		a[i]=false;
//}

int main(){
	int t,i,j,l,dem;
	char c[102];

	ifstream in("input.in");
	ofstream out("output.out");
	in>>t;
	in.getline(c,0);
	for (i=1; i<=t; i++){
		dem =0;
		in.getline(c,101);
		l=strlen(c);
		if (c[l-1]=='-') dem =1;
		for (j=1; j<l ; j++){
			if (c[j]!=c[j-1]) dem ++;
		}
		out<<"Case #"<<i<<": "<<dem<<endl;
	}

	return 0;
}
