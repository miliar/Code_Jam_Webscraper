#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

int main(){
	ifstream in;
	string ss;
	cin>>ss;
	in.open(ss.c_str());
	int n;
	in>>n;
	int  asd[n];
	for(int i=0;i<n;i++){
		asd[i]=0;
		int k;
		in>>k;
		string s;
		in>>s;
		int aval=0;
		for(int j=0;j<=k;j++){
			int currentNeed=j;
			char c = s[j];
			int a= (int)(c-'0');
			//cout<<a<<" * "<<aval<<" * "<<currentNeed<<" \n";
			if(currentNeed>aval && a!=0){
				asd[i]=asd[i]+currentNeed-aval;
				aval=currentNeed;
			}
			aval=aval + a;
		}
		
	}
	in.close();
	ofstream out;
	string outFile="test.out";
	out.open(outFile.c_str());
	for(int i=0;i<n;i++){
		out<<"Case #"<<i+1<<": "<< asd[i]<<"\n";
	}
	out.close();
	return 0;
}
