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


string check( int A,  int B,  int K)
{
	int res = 0;
	REP(i,A)
	{
		REP(j,B)
		{
			if((i&j)<K) res++;
		}
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
		 int A,B,K;
		 in >> A >> B >> K;
		res.PB(check(A,B,K));
	}
			
				
	
	stringstream ss;
	REP(i,res.S)
	{
		ss << "Case #" << i+1 << ": " << res[i] << endl;
	}
	
	cout << ss.str();




}


