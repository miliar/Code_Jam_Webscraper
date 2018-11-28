#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <time.h>
#include <string.h>
#include <limits.h>
#include <stdio.h>

using namespace std;

#define FOR(i,a,b)  for(int i = (a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define S           size()
#define PB          push_back
#define ALL(a)      a.begin(),a.end()
#define MP          make_pair
#define V           vector
#define VI          V < int > 
#define VVI         V < VI >
#define VVVI		V < VVI >
#define VL			V < long long > 
#define VVL			V < VL >
#define VD          V < double >
#define VF          V < float >
#define VS			V < string >


VI red(string s)
{
	VI res;
	char c=s[0];
	res.PB(1);
	int idx = 0;
	FOR(i,1,s.S)
	{
		if(c==s[i]) {res[idx]+=1; continue;}
		c=s[i];
		res.PB(1);
		++idx;
	}
	return res;
}

string reduce(string s)
{
	string res="";
	char c=s[0];
	res+=c;
	FOR(i,1,s.S)
	{
		if(c==s[i]) continue;
		c=s[i];
		res+=c;
	}
	return res;
}


string check(VS s)
{
	string f = reduce(s[0]);
	VVI m;
	VI vf = red(s[0]);
	m.PB(vf);
	FOR(i,1,s.S)
	{
		string g = reduce(s[i]);
		if(g!=f) return "Fegla Won";
		VI vg = red(s[i]);
		m.PB(vg);
	}
	
	int res = 0;
	double sum = 0;
	REP(i,m[0].S)
	{
		sum = 0;
		REP(j,m.S)
		{
			sum += m[j][i];
		}
		double avg = sum/m.S;
		int hi = ceil(avg);
		int lo = floor(avg);
		
		int h=0,l=0;
		REP(j,m.S)
		{
			h+=abs(hi-m[j][i]);
			l+=abs(lo-m[j][i]);
		}
		
		if(h<l){res+=h;}
		else {res+=l;}
	}
		
		
	stringstream ss;	
	ss << res;
	
	return ss.str();

}

int main(int argc, char** argv)
{
	int n;
	++argv;
	ifstream in(*argv);
	
	in >> n;
	VS res;
	string N,L;
	REP(i,n)
	{
		int N;
		in >> N;
		VS str;
		REP(j,N)
		{
			string s;
			in >> s;
			str.PB(s);
		}
		res.PB(check(str));
	}
			
				
	
	stringstream ss;
	REP(i,res.S)
	{
		ss << "Case #" << i+1 << ": " << res[i] << endl;
	}
	
	cout << ss.str();




}


