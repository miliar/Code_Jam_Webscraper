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

double C, F, X;

double get_ans( int farms )
{
	double re = 0.;
	FOR(a,0,farms-1)
		re += C/(2.+F*a);
	re += X/(2.+F*farms);
	return re;
}

void stupid()
{
	double ans = X;
	FOR(a,0,5000)
	{
		double tmp =  get_ans(a);
		//WR("%.10lf\n", tmp);
		ans = min( ans, tmp );
	}
	WR("%.10lf", ans);
}

void sol()
{
	double ans = X/2.;
	double re = 0., tmp;
	bool flag = false;
	FOR(a,0,o_O)
	{
		re += C/(2.+F*a);
		tmp = re + X/(2.+F*(a+1));
		ans = min( ans, tmp );
		if (tmp > ans)
		{
			flag = true;
			break;
		}
	}
	if (!flag) cerr << "may be wrong\n";
	WR("%.10lf", ans);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin >> t;
	FOR(a,1,t)
	{
		cerr << a << "\n";
		cin >> C >> F >> X;
		cout << "Case #" << a << ": ";
		//stupid();
		//cout << " ";
		sol();
		cout << "\n";
	}
	return 0;
}
