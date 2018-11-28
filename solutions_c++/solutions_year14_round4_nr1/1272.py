#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int DEBUG=0;
int u[10001];

int doit(int N, vector<int> v, int cap) {
	sort(v.begin(),v.end());
	cout<<N<<endl;
	for(int i=0;i<N;i++) u[i]=0;
	int ret=0;
	for(int i=0;i<N;i++) if(!u[i]) {
		bool done=false;
		for(int j=N-1;j>=0;j--) if(!u[j] && v[i]+v[j]<=cap) {
			done=true;
			u[i]=true;
			u[j]=true;
			ret++;
			break;
		}
		if(!done) {
			ret++;
			u[i]=true;
		}
	}
	return ret;
}

int main()
{
	ifstream infile;
	string prefix = "A-large";
	infile.open(prefix + ".in");
	ofstream outfile(prefix + ".out");
	int cases;
	if (infile.is_open()) {
		infile>>cases;
	}
	else {
		return 0;
	}
	for(int i=0;i<cases;i++) {
		int N;
		infile >> N;
		int X;
		infile >> X;
		vector<int> v;
		for(int j=0;j<N;j++) {
			int z;
			infile>>z;
			v.push_back(z);
		}
		outfile << "Case #" << (i+1) << ": " << doit(N,v,X) << endl;
	}
	cout<<"DONE"<<endl;
	string zzz;
	cin>>zzz;
	outfile.close();
	return 0;
}