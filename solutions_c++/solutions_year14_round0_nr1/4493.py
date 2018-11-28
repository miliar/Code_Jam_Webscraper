/* Brian's GCJ entries */
#include <vector>
#include <iterator>
#include <map>
#include <cmath>
#include <set>
#include <deque>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;
int bitct(long long r) {return r == 0 ? 0 : (bitct(r>>1) + (r&1));}
long long gcd(long long x, long long y) {return x ? gcd(y%x,x) : y;}
template<typename T> ostream& operator << (ostream &o,vector<T> v) {o<<"{";
	int i=0,s=v.size();for(;i+1<s;i++)o<<v[i]<<", ";if(s)o<<v[i];o<<"}";return o;}
long long choose(long long n, long long q)
{ if(n==0 || q==0) return 1;
	if (q==1) return n; else return ( choose(n, q-1) * (n-q+1 ) /q); }
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define FOR(i,a,b) for(typeof(a) i=(a); i < (b); ++i)
//int dx[8] = {0,  1,  1,  1,  0, -1, -1, -1}
//int dy[8] = {1,  1,  0, -1, -1, -1,  0,  1}
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

void calc(ifstream &, ofstream &);
main() { stringstream filename, fnamein, fnameout;
	string file("A");
	filename << file << "-small.";
	fnamein << filename.str() << "in"; fnameout << filename.str() << "out";
	ifstream fin(fnamein.str().c_str()); ofstream fout(fnameout.str().c_str());
	int count;
	fin >> count;
	for(int i=0;i<count;i++) {
		fout << "Case #" << (i+1) << ": ";
		calc(fin, fout);
		fout.flush(); }
	fin.close(); fout.close(); }

void calc(ifstream &fin, ofstream &fout)
	{
	int poss[4];

	int guess=0;
	fin >>guess;
	for(int i=1;i<guess;i++)
		{
		for(int j=0;j<4;j++)
			{
			int inv;
			fin >> inv;
			}

		}

	for(int j=0;j<4;j++)
	{
		int inv;
		fin >> inv;
		poss[j] =inv;
	}
	 
	for(int i= guess+1;i<= 4;i++)
		{
		for(int j=0;j<4;j++)
			{
			int inv;
			fin >> inv;
			}

		}

	fin >> guess;
	int possn=0;
	int possv=0;
	
	for(int i=1;i<guess;i++)
		{
		for(int j=0;j<4;j++)
			{
			int inv;
			fin >> inv;
			}

		}

	for(int j=0;j<4;j++)
	{
		int inv;
		fin >> inv;
		for(int i=0;i<4;i++)
			{
			if(poss[i] == inv)
				{
				possv = inv;
				possn++;
				}
			}
	}
	 
	for(int i= guess+1;i<= 4;i++)
		{
		for(int j=0;j<4;j++)
			{
			int inv;
			fin >> inv;
			}

		}

	if(possn == 0)
		fout << "Volunteer cheated!" << endl;
	else if (possn>1)
		fout << "Bad magician!" << endl;
		else
		fout << possv << endl;

	return; 
	}
