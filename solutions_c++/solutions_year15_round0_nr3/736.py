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
	fin.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\C-large.in", ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\C-large.out", ios::out);

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

	char a[10001];
	int m[5][5] = { {0, 0, 0, 0, 0}, {0, 1, 2, 3, 4 }, { 0, 2, -1, 4, -3 }, { 0, 3, -4, -1, 2 }, { 0, 4, 3, -2, -1 } };
	fin >> casecnt;
	FRE(e, 1, casecnt) {
		long long l, x;
		fin >> l >> x;
		fin >> a;
		int s = 1;
		map<long long, long long> mm;
		long long t = 0;
		mm[s] = t;
		bool found = false;
		string ret = "NO";
		for (t = 1; t<=x;) {
			FR(i, 0, l) {
				s = (s>0) ? m[s][a[i] - 'g'] : -m[-s][a[i] - 'g'];
			}
			if (mm.find(s) != mm.end() && !found) {
				long long n = (x - mm[s])/(t - mm[s]) + 1;
				t = mm[s] + (n - 1)*(t - mm[s]) + 1;
				found = true;
			}
			else {
				mm[s] = t;
				t++;
			}
		}

		if (s == -1) {
			long long si = -1, sk = -1;
			s = 1;
			FR(i, 0, 500) {
				FR(j, 0, l) {
					s = (s>0) ? m[s][a[j] - 'g'] : -m[-s][a[j] - 'g'];
					if (s == 2) {
						si = i*l + j;
						break;
					}
				}
				if (si != -1) {
					break;
				}
			}
			if (si != -1) {
				s = 1;
				FR(i, 0, 500) {
					for (int j = l - 1; j >= 0; j--) {
						s = (s > 0) ? m[a[j] - 'g'][s] : -m[a[j] - 'g'][-s];
						if (s == 4) {
							sk = x*l - (i + 1)*l + j;
							break;
						}
					}
					if (sk != -1) {
						if (si < sk) {
							ret = "YES";
						}
						break;
					}
				}
			}
		}

		fout << "Case #" << e << ": " << ret << endl;
		cout << "Case #" << e << ": " << ret << endl;
	}

	return 0;
}