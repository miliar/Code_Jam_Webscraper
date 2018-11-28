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



void preWork()
{
	//  test longInt;

	LongInt a="123456789";
	LongInt b="987654321";
	LongInt c,d;
	c= b.modDivide(a,&d);
	
	cout<<c<<endl;
	cout<<d<<endl;
}

void work()
{
	int n,m;
	fin>>n>>m;
	int z[200][200];
	bool ok[200][200];
	memset(ok,false,sizeof(ok));
	for (int i=0; i<n; i++) {
		int x = 0;
		for (int j=0; j<m; j++) {
			fin>>z[i][j];
			if (z[i][j] > x) x = z[i][j];
		}
		for (int j=0; j<m; j++) {
			if (z[i][j] ==x) ok[i][j] = true;
		}
	}
	for (int j=0; j<m; j++) {
		int x = 0;
		for (int i=0; i<n; i++) {
			if (z[i][j] > x) x = z[i][j];
		}
		for (int i=0; i<n; i++) {
			if (z[i][j] ==x) ok[i][j] = true;
		}
	}
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			if (!ok[i][j]) 
			{
				fout<<"NO";
				return;
			}
		}
	}
	fout<<"YES";
}