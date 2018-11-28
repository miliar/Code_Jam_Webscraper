#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000

void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int n;
double V[110], T[110];
double eps = 0.000001;

void sol()
{
	if (n==1)
	{
		if (abs(T[0]-T[1]) > eps) cout << "IMPOSSIBLE";
		else WR("%.10lf", V[0]/V[1]);
	}
	else if (n==2)
	{
		if (T[1] > T[2])
		{
			swap( T[1], T[2] );
			swap( V[1], V[2] );
		}

		if (T[1]-T[0] > eps || T[2]-T[0] < -eps) cout << "IMPOSSIBLE";
		else
		{
			if (abs( T[1]-T[2] ) < eps)
			{
				WR("%.10lf", V[0]/(V[1]+V[2]));
			}
			else if (abs( T[1]-T[0] ) < eps)
			{
				WR("%.10lf", V[0]/V[1]);
			}
			else if (abs( T[0]-T[2] ) < eps)
			{
				WR("%.10lf", V[0]/V[2]);
			}
			else
			{
				double koeff = (T[2]-T[0]) / (T[0]-T[1]);
				if (V[1] > koeff*V[2]) WR("%.10lf", V[0]/(V[2]*koeff+V[2]));
				else WR("%.10lf", V[0]/(V[1]+V[1]/koeff));
			}
		}
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t=0;
	cin >> t;
	FOR(a,1,t)
	{
		cerr << a << "\n";
		
		cin >> n >> V[0] >> T[0];
		FOR(b,1,n) cin >> V[b] >> T[b];

		cout << "Case #" << a << ": ";

		sol();

		cout << "\n";
	}

	cerr << clock() << "\n";
	return 0;
}
