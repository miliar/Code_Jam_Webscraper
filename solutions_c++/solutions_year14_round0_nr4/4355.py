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
#include <string.h>
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

void calc(ifstream &, ofstream &);
main() { stringstream filename, fnamein, fnameout;
	string file("D");
	filename << file << "-small.";
	fnamein << filename.str() << "in"; fnameout << filename.str() << "out";
	ifstream fin(fnamein.str().c_str()); ofstream fout(fnameout.str().c_str());
	int countx;
	fin >> countx;
	for(int i=0;i<countx;i++) {
		fout << "Case #" << (i+1) << ": ";
		calc(fin, fout);
		fout.flush(); }
	fin.close(); fout.close(); }


void calc(ifstream &fin, ofstream &fout)
	{
	int N;

	fin >> N;
	double NB  [N], KB  [N];

	for(int i=0;i<N;i++)
		{
		double inv;
		fin >> inv;
		NB  [i] = inv;
		}
	for(int i=0;i<N;i++)
		{
		double inv;
		fin >> inv;
		KB  [i] = inv;
		}
		
		sort(NB, NB+N);
		sort(KB, KB+N);

		int d=0, w=0;

		cout << vector<double>(NB, NB+N) << endl << vector<double>(KB , KB+N) << endl;

	int j=0;
	for(int i=0;i<N;i++)
		{
		if(NB[i] > KB[j])
			{
			j++;
			d++;
			}
		}

	set<double> kb(KB, KB+N);
	for(int i=0;i<N;i++)
		{
		double mnb = NB[N-1-i];

		auto xx = kb.lower_bound(mnb);
		if(xx == kb.end())
			{
			w++;
			continue;
			}
		else
			{
			kb.erase(xx);
			}

		}
		




	fout << d << " " << w << endl;
		
	return; 
	}
