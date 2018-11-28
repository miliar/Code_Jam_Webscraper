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

int assign[10];
int cache[1024];
int mx=0;
int ways=0;

int eval(vector<string> &v) {
	set<string> s;
	for(int i=0;i<v.size();i++) {
		for(int j=0;j<=v[i].size();j++) s.insert(v[i].substr(0,j));
	}
	return s.size();
}

void doit2(vector<string> &v, int servers, int idx) {
	//if(idx==v.size()) return;
	if(idx==v.size()) {
		int ret=0;
		for(int i=0;i<servers;i++) {
			int mask=0;
			for(int j=0;j<v.size();j++) {
				if(assign[j]==i) mask+=(1<<j);
			}
			if(mask==0) return;
			ret+=cache[mask];
		}
		if(DEBUG&&ret==10) {
			for(int i=0;i<v.size();i++) cout<<assign[i]<<" "; cout<<endl;
		}
		if(ret>mx) { 
			mx=ret;
			ways=1;
		}
		else if(ret==mx) {
			ways++;
		}
		return;
	}
	for(int i=0;i<servers;i++) {
		assign[idx]=i;
		doit2(v,servers,idx+1);
	}
}

pair<int,int> doit(vector<string> v, int servers) {
	mx=0;
	ways=0;
	int n=v.size();
	for(int i=0;i<(1<<n);i++) {
		vector<string> w;
		for(int j=0;j<n;j++) if(((1<<j)&i)>0) {
			w.push_back(v[j]);
		}
		cache[i]=eval(w);
	}
	doit2(v,servers,0);
	return make_pair(mx,ways);
}

int main()
{
	ifstream infile;
	string prefix = "D-small-attempt2";
	//string prefix = "practice";
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
		int servers;
		infile >> servers;
		vector<string> v;
		for(int j=0;j<N;j++) {
			string z;
			infile>>z;
			v.push_back(z);
		}
		DEBUG=(i==0);
		pair<int,int> ret=doit(v,servers);
		outfile << "Case #" << (i+1) << ": " << ret.first << " " << ret.second << endl;
	}
	cout<<"DONE"<<endl;
	string zzz;
	cin>>zzz;
	outfile.close();
	return 0;
}