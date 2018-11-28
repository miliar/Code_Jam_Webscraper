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


bool palindromes(int a)
{
	vector <int> vi;
	while(a)
	{
		vi.push_back(a%10);
		a /= 10;
	}

	FOR(i,0,vi.size()/2)
	{
		if(vi[i] != vi[vi.size() - i -1])
			return false;
	}

	return true;
}


bool solve(istream &in,ostream &out)
{
	LL T;
	in >> T;

	int sqPalindromes[1001][2] = {0};
	int j = 0;
	FOREQ(i,1,31)
	{
		int sq = i*i;
		if(palindromes(i) && palindromes(sq))
		{
			j++;
			sqPalindromes[sq][0] = j;
			sqPalindromes[sq][1] = 1;
		}
	}

	j = 0;
	FOREQ(i,1,1000)
	{
		if(0 == sqPalindromes[i][0])
			sqPalindromes[i][0] = j;
		else
			j = sqPalindromes[i][0];
	}

	FOR(i,0,T)
	{
		int A,B;
		int rt = 0;
		in >> A >> B;

		out << "Case #"<<i+1<<": "<< sqPalindromes[B][0] -  sqPalindromes[A][0] +  sqPalindromes[A][1];

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
