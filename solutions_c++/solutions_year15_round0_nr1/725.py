// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;

#define SWAP(a,b,t) (t)=(a);(a)=(b);(b)=(t);
#define MAX(a,b)	((a)>(b))?(a):(b)
#define MIN(a,b)	((a)<(b))?(a):(b)
#define FR(i,a,b)	for(int ( i)=(a); ( i)<(b); ++( i))
#define FRE(i,a,b)	for(int ( i)=(a); ( i)<=(b); ++( i))
#define FRD(i,a,b)	for(( i)=(a); ( i)<(b); ++( i))
#define FRI(i,a)	for(( i)=(a).begin(); ( i)!=(a).end(); ++( i))
#define SWAP(a,b,t) (t)=(a);(a)=(b);(b)=(t);

#define I __int64
#define VI vector<int>
#define VL vector<I>
#define VD vector<double>
#define VLD vector<long double>
#define VS vector<string>
#define LI list<int>
#define LL list<I>
#define LD list<double>
#define LLD list<long double>
#define LS list<string>
#define SI set<int>
#define SL set<I>
#define SD set<double>
#define SLD set<long double>
#define SS set<string>
#define MII map<int,int>
#define MIL map<int,I>
#define MID map<int,double>
#define MIS map<int,string>
#define MLL map<I,I>
#define MLI map<I, int>
#define MLD map<I,double>
#define IT iterator

#define MMS(a) memset(a,0,sizeof(a))


int main(int argc, _TCHAR* argv[]) {
	fstream fin, fout;

	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\A-large.in", ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\A-large.out", ios::out);

	if (!fin.good())
	{
		cout << "Input file not opened" << endl;
		exit(-1);
	}
	if (!fout.good())
	{
		cout << "Output file not opened" << endl;
		exit(-1);
	}


	fin >> casecnt;
	FRE(e, 1, casecnt) {
		int smax;
		char s[1002];
		fin >> smax >> s;
		int t = s[0] - '0', ret = 0;
		FRE(i, 1, smax) {
			if (i > t) {
				ret += i - t;
				t = s[i] - '0' + i;
			}
			else {
				t += s[i] - '0';
			}
		}
		fout << "Case #" << e << ": " << ret << endl;
		cout << "Case #" << e << ": " << ret << endl;
	}

	return 0;
}