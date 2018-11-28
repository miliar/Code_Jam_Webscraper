#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

vector<long long> func(int k, int c, int s){
	vector<long long> res;
	for (int i=1;i<=s;++i){
		res.push_back(i);
	}
	return res;
}

int main(){
	ofstream myfile;
  	myfile.open ("outputd.txt");
	int t;
	cin>>t;
	for (int i=1;i<=t;++i){
		int k,c,s;
		cin>>k>>c>>s;
		vector<long long> res=func(k,c,s);
		myfile<<"Case #"<<i<<": ";
		if (res.size()==0) myfile<<"IMPOSSIBLE";
		else{
			for (int j=0;j<res.size();++j){
				myfile<<res[j]<<' ';
			}
		}
		myfile<<endl;
	}
	myfile.close();
	return 0;
}
