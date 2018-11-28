// solution for 

#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <cassert>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#include <cstdio>
#include <map>
#include <deque>
#include <vector>
#include <set>
#include <cstring>
#include <algorithm>
#include <iomanip>

using namespace std;

// setiosflags(ios¡Ëscientific)
// setw()
// setfill('x')
// setioflags(ios::showpos)
// setiosflags(ios¡Ëright)

#define COUT_HEX(x) hex << x
#define COUT_F_PRE(n,f) setiosflags(ios::fixed)<<setprecision(n)<<f
#define ZERO(n) memset(n,0,sizeof(n))
#define M1SET(n) memset(n,-1,sizeof(n))
#define MIN(m,n) ((m<n)?m:n)
#define MAX(m,n) ((m>n)?m:n)

#define UL unsigned long long
#define UI unsigned int
#define LL long long

#define FOR(i,a,b)   for(LL(i) = (LL)(a);(i) < (LL)(b);(i)++)
#define FOREQ(i,a,b) for(LL(i) = (LL)(a);(i) <= (LL)(b);(i)++)
#define RFOR(i,a,b)  for(LL(i) = (a), _b(b);(i) >= _b; --(i))
//#define FOREACH(c,itr) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end();itr++)
#define ALL(a)   (a).begin(),(a).end()
#define SZ(a)	 ((int)(a).size())

#define MO 1000000007UL

#define MOD(i) (i = ((i >= MO) ? i%MO : i))

int h[101][101];
int N,M;
int maxr[101];
int maxc[101];

int check()
{

	FOR(i,0,N)
	{
		int max = 0;
		FOR(j,0,M)
		{
			if(max < h[i][j])
				max = h[i][j];
		}
		maxr[i] = max;
	}

	FOR(i,0,M)
	{
		int max = 0;
		FOR(j,0,N)
		{
			if(max < h[j][i])
				max = h[j][i];
		}
		maxc[i] = max;
	}

	FOR(i,0,N)
	{
		int max = 0;
		FOR(j,0,M)
		{
			if(h[i][j] < maxr[i] && h[i][j] < maxc[j])
				return 0;
		}
	}
	return 1;
}

bool solve(istream &in,ostream &out)
{
	LL T;
	in >> T;


	FOR(i,0,T)
	{
		in >> N >> M;
		FOR(j,0,N)
		{
			FOR(k,0,M)
				in >> h[j][k];
		}

		out << "Case #"<<i+1<<": ";
		switch(check())
		{
			case 1:
				out << "YES";
				break;
			case 0:
				out << "NO";
				break;
		}
		out << endl;
	}

	return true;
}


int main()
{
	bool bSolved;
	time_t timeBegin = time(NULL);

	#ifndef ONLINE_JUDGE
	ifstream in("in.in");
	ofstream out("out.out");
	bSolved = solve(in,out);
	#else
	bSolved = solve(cin,cout);
	#endif
	

	#ifndef ONLINE_JUDGE
	in.close();
	if(!bSolved)
		cout << "not solved Time: " << time(NULL) - timeBegin << endl;
	else
		cout << "solved Time:" << time(NULL) - timeBegin <<endl;
	system("pause");
	#endif
	
	return 0;
}
