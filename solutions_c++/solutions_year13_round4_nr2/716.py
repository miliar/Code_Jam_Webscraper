//#include "LongInt.h"
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
#include <ctime>
using namespace std;
ifstream fin; 
ofstream fout;

//  越界 问题  浮点 除 变 整除，  abs 问题


void preWork();
void work();
void work1();
int sorttime;
int main(int argc, char *argv[])
{
	//preWork();
	QCoreApplication a(argc, argv);

	//	char * inputName="A-large.in";
	//	fin.open(inputName);
	//	fin.open ( "A-small-practice.in");
	//fin.open ( "A-large-practice.in");
	fin.open ( "input.txt");

	int now =clock();
	sorttime=0;
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
	int now2= clock();
	
	cout<<now<<endl<<now2<<endl<< now2-now<<endl;
	cout<<sorttime<<endl;

	//	return a.exec();
}


void preWork()
{


}
long long int n,total;
bool check1(long long int m, long long int p) {
	long long int pool = m;
	int z[100];
	long long int t = 0;
	for (int i=0; i<n; i++) {
		t*=2;
		if (pool>0) {
			z[i] = 1;
			pool = (pool-1)/2;
		}
		else {
			z[i] = 0;
		}
		t+=z[i];
	}
	if (t<p) return true;
	return false;
}
bool check2(long long int m, long long int p) {
	long long int pool = total-1-m;
	int z[100];
	long long int t = 0;
	for (int i=0; i<n; i++) {
		t*=2;
		if (pool>0) {
			z[i] = 0;
			pool = (pool-1)/2;
		}
		else {
			z[i] = 1;
		}
		t+=z[i];
	}
	if (t<p) return true;
	return false;
}
void work()
{
	long long int p,   l,r,m;
	total = 1;
	fin>>n>>p;
	for (int i=0; i<n; i++) total*=2;
	l = 0;
	r = total ;
	while(l<r-1) {
		m = (l+r)/2;
		if (check1(m,p)) {
			l=m;
		}
		else {
			r=m;
		}
	}
	fout<<l<<' ';
	l = 0;
	r = total ;
	while(l<r-1) {
		m = (l+r)/2;
		if (check2(m,p)) {
			l=m;
		}
		else {
			r=m;
		}
	}
	fout<<l;
}

