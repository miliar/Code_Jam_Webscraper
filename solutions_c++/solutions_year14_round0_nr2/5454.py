#pragma comment(linker, "/STACK:64000000")
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <deque>
#include <algorithm>
#define _USE_MATH_DEFINES
#include <math.h>
using namespace std;
#define forn(i,n) for (LL i=0;i<n;i++)
#define rforn(i,n) for (LL i=n-1;i>=0;i--)
#define mp make_pair
#define __int64 long long
#define LL long long

int main()
{
	ios_base::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif

	int T;
	cin>>T;

	double c,f,x, curt, rate, mint, tt;
	forn(t,T)
	{
		cin>>c>>f>>x;

		rate=2;
		curt=0;
		mint=curt+x/rate;

		for (double d=0;d<100000; d++)
		{
			curt+=c/rate;
			rate+=f;

			tt=curt+x/rate;
			mint=min(mint,tt);
		}
		printf("Case #%d: ",(t+1));
		printf("%.8lf\n",mint);
	}
}