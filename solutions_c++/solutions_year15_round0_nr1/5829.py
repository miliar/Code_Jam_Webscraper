#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;
int main(int argc, char **argv)
{
	int T;
	int N;
	int noc,ad;
	string c;
	vector<int> list;
	ifstream infile;
	ofstream outfile;
	infile.open("A-small-attempt0.in",ios::in);
	outfile.open("a.out",ios::out);

	if(!infile.is_open()) {cout<<"File not found"; cin>>T;return 0;}
	infile>>T;
for (int t=1;t<=T;t++){
	noc=0;
	ad=0;
	infile>>N;
	
		infile>>c;
		for (int n=0;n<=N;n++)
	{
		list.push_back((int)c[n]-'0');
	}
	int cur=0;
	for (vector<int>::iterator vv =list.begin();vv!=list.end();vv++){
		
		if(noc>=cur) noc+=*vv;
		
		else if(*vv>0) {ad+=(cur-noc);noc=cur+*vv;}
		
		cur++;
	}
	cout<<"Case #"<<t<< ": "<<ad<<"\n";
	outfile<<"Case #"<<t<< ": "<<ad<<"\n";
	list.clear();
}
	infile.close();
	outfile.close();
}