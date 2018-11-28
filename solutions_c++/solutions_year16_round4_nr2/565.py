// 2011_2.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <functional>
#include <vector>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <bitset>
#include <list>
#include <iomanip>      // std::setprecision

using namespace std;

FILE * in, *out;

#define fo(a,b,c) for(int a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

#define LL long long

int ri() { int a; fscanf(in, "%d", &a); return a; }
double rf() { double a; fscanf(in, "%lf", &a); return a; }
char sbuf[100005];
string rstr()
{
	//fscanf(in, "%lf", sbuf); 
	char c;
	char * b = sbuf;
	while (c = fgetc(in))
	{
		if (c == '\n' || c == 255) break;
		*b++ = c;
	}
	*b = 0;
	return sbuf;
}


int nod(int a, int b)
{
	if (a == 1 || b == 1) return 1;
	if (a == 0) return b;
	if (b == 0) return a;

	return nod(b%a, a);
}

vector<int> primes;
void calculatePrimes()
{
	primes.push_back(2);
	for (int i = 3; i < 500; i += 2)
	{
		bool bFound = false;
		int m = (int)sqrt((float)i);
		for (int j = 1; j < primes.size() && !bFound && primes[j] <= m; j++)
			bFound = ((i%primes[j]) == 0);
		if (!bFound)
			primes.push_back(i);
	}
}


void getVotesProb(vector<double> & p, int f, int t, vector < double > & res)
{
	if (t - f == 0)
	{
		res.push_back(1);
		return;
	}
	if (t - f == 1)
	{
		res.push_back(1-p[f]);
		res.push_back(p[f]);
		return;
	}
	vector < double > v1;
	vector < double > v2;
	res.resize(t - f + 1);
	int m = (f + t) / 2;
	getVotesProb(p, f, m, v1);
	getVotesProb(p, m, t, v2);
	for (int i = 0; i < v1.size(); i++)
		for (int j = 0; j < v2.size(); j++)
			res[i + j] += v1[i] * v2[j];
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int n, k;
		cin >> n >> k;
		vector < double > p(n);
		fi(n) cin >> p[i];
		k /= 2;

		sort(p.begin(), p.end());

		double bestprob = 0;
		for (int i = 0; i <= n; i++)
		{
			for (int j = 0; j <= n; j++)
			{
				if (i + j + 2 * k > n) break;
				vector < double > v1;
				vector < double > v2;
				getVotesProb(p, i, i+k, v1);
				getVotesProb(p, n-j-k, n-j, v2);

				double curprob = 0;
				for (int i = 0; i <= k; i++)
					curprob += v1[i] * v2[k - i];
				if (curprob > bestprob)
					bestprob = curprob;
			}

		}

		for (int i = 0; i <= 2*k; i++)
		{
			vector < double > v1;
			vector < double > v2;
			getVotesProb(p, 0, i, v1);
			getVotesProb(p, n - 2*k+i, n, v2);

			double curprob = 0;
			for (int i = 0; i <= k; i++)
			{
				if (v1.size() <= i) break;
				if (v2.size() <= k - i) continue;
				curprob += v1[i] * v2[k - i];
			}
			if (curprob > bestprob)
				bestprob = curprob;
		}
		
		if (bestprob < 1.0e-7)
			cout << "Case #" << t << ": " << setprecision(7) << setiosflags(ios::fixed | ios::showpoint) << 0 << endl;
		else
		cout << "Case #" << t << ": " << setprecision(7) << setiosflags(ios::fixed | ios::showpoint) << bestprob << endl;

	}


	return 0;
}