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
#include <iomanip>  
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

/*
#define MX 1000001

long long cnt[MX];
long long p[MX];


int fn(int c2, int c3, int n) {
	int ret = 0;
	if (n > 0) {
		if (n < c2) {
			ret = 2 * n;
		}
		else {
			ret = 2 * c2;
			n -= c2;
			if (n < c3) {
				ret += 3 * n;
			}
			else {
				ret += 3 * c3;
				n -= c3;
				ret += 4 * n;
			}
		}
	}
	return ret;
}

int main(int argc, _TCHAR* argv[]) {
	fstream fin, fout;

	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\B-large-practice.in", ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\B-large-practice.out", ios::out);

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
		int r,c,n;
		fin >> r>>c>>n;
		int ret = 0;

		int c2 = 0, c3 = 0, c4 = 0;
		if (c == 1 || r == 1) {
			c2 = max(r / 2, c / 2);
			ret = fn(c2, c3, n-(r*c + 1) / 2);
			if ((c % 2 == 0 || r % 2 == 0 ) && ret)
				ret--;
		}
		else if (c % 2 == 0 || r % 2 == 0) {
			c2 = 2;
			c3 = c - 2 + r - 2;
			ret = fn(c2, c3, n-(r*c + 1) / 2);
		}
		else {
			c2 = 4;
			c3 = r - 3 + c - 3;
			ret = min(fn(0, r-1+c-1, n-(r*c+1) / 2), fn(c2, c3, n-(r*c) / 2));
		}

		cout << "Case #" << e << ": " << r << ", " << c << ", " << n << "->" << ret << " .. " << ret << endl;
		fout << "Case #" << e << ": " << ret << endl;
	}
	return 0;
}
*/

/*
int main(int argc, _TCHAR* argv[]) {
	fstream fin, fout;

	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\B-large-practice.in", ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\B-large-practice.out", ios::out);

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
		int ret = 0;
		int n;
		fin >> n;
		vector<pair<int, int> > s;
		int t;
		FR(i, 0, n) {
			int dd,h,m;
			fin >> dd>>h>>m;
			FR(j, 0, h) {
				s.push_back(pair<int, int>(m + j, dd));
			}
		}
		sort(s.begin(), s.end());
		t = s.size()-1;
		if (s[0].first != s[t].first) {
			if ()
		}
		cout << "Case #" << e << ": " << ret << endl;
		fout << "Case #" << e << ": " << ret << endl;

	}
}
*/

/*
int divide(int r, int w) {
	int ret = 0;
	int rem = r - w;
	while (rem > 1) {
		ret++;
		rem /= 2;
	}
	ret += w;
	return ret;
}

int ss(int r, int w) {
	int ret = 0;
	for (int i = 0; i*w< r; i++) {
		ret = max(i+divide(r - w*i, w), ret);
	}
	return ret;
}

int main(int argc, _TCHAR* argv[]) {
	fstream fin, fout;

	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\A-small-attempt0.in", ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\A-small-attempt0.out", ios::out);

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
		int r,c,w,ret = 0;
		fin >> r >> c >> w;
		FR(i, 0, r) {
			if (i == r - 1) {
				ret += ss(c, w);
			}
			else {
				ret += (c - w) / w + 1;
			}
		}
		cout << "Case #" << e << ": " << ret << "," << c <<":"<<w<<endl;
		fout << "Case #" << e << ": " << ret << endl;
	}
}
*/

int main(int argc, _TCHAR* argv[]) {
	fstream fin, fout;

	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\B-small-attempt0.in", ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\B-small-attempt0.out", ios::out);

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
		long double ret = 0.0;
		int k, l, s;
		int cnt[26];
		MMS(cnt);
		fin >> k >> l >> s;
		char str[102];
		fin >> str;
		FR(i, 0, k)  {
			cnt[str[i] - 'A']++;
		}
		fin >> str;
		string ts = str;
		bool done = false;
		FR(i, 0, l) {
			if (cnt[str[i] - 'A'] == 0) {
				done = true;
				break;
			}
		}

		if (!done) {
			long double df = 1.0;
			FR(i, 0, l) {
				df *= 1.0*cnt[str[i]-'A'] / k;
			}
			int tot = 0, sz = l;
			FR(i, 1, l) {
				string s1 = ts.substr(0, l-i);
				string s2 = ts.substr(i);
				if (s1 == s2) {
					sz = i;
					break;
				}
			}
			ret = ((s - l)/sz + 1) - df*(s-l+1);
		}
		cout << "Case #" << e << ": " << std::setprecision(12) << ret << endl;
		fout << "Case #" << e << ": " << std::setprecision(12) << ret << endl;
	}
}