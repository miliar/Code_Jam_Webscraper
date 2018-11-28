#include "LongInt.h"
#include <QtCore/QCoreApplication>
#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <algorithm>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <cassert>
#include <cmath>
using namespace std;
ifstream fin; 
ofstream fout;

void preWork();
void work();

int main(int argc, char *argv[])
{
	preWork();
	QCoreApplication a(argc, argv);

//	char * inputName="A-large.in";
//	fin.open(inputName);
//	fin.open ( "A-small-practice.in");
	//fin.open ( "A-large-practice.in");
	fin.open ( "NO1_input.txt");
	
	fout.open("output.txt");
	int n;
	fin >>n;
	for (int i=0; i<n; i++)
	{
		fout<<"Case #"<<i+1<<": ";
		work();
		fout<<endl;
	}


	fin.close();

	fout.close();



//	return a.exec();
}

vector<long long int> zz;
bool palin(long long int t) {
	string s;
	while(t>0) {
		s+='0'+t%10;
		t/=10;
	}
	bool ok = true;
	for (int i=0; i<s.size(); i++) {
		if (s[i] != s[s.size()-i-1]) {
			ok = false;
			break;
		}
	}
	return ok;
}
void preWork()
{
	long long int x,t;
	for (x = 1; x<= 10000000; x++) {
		if (palin(x) && palin(x*x)) zz.push_back(x*x);
	}
}

void work()
{
	long long int a,b;
	fin>>a>>b;
	int re = 0;
	for (int i=0; i<zz.size(); i++) {
		if (zz[i]>=a && zz[i]<=b) re++;
	}
	fout<<re;
}