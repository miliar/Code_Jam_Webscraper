///*

#include<stdio.h>
#include<iostream>
#include<iomanip>
#include<fstream>
#include<string>
#include<vector>
#include<set>
#include<stack>
#include<list>
#include<queue>
#include<deque>
#include<bitset>
#include<map>
#include<algorithm>
#include<cmath>
\
#include<numeric>

//#pragma comment (linker, "/STACK:640000000")
#define INF 1000000000 //1e10
#define EPS 1e-6
#define PI 3.1415926535897932384626433832795028841971
#define mp make_pair
#define pb push_back
#define pf push_front
#define ppf pop_front
#define ppb pop_back
#define x first
#define y second
#define pii pair<int,int>
#define pdd pair<double,double>
#define FOR(i,a,b) for (int _n(b), i(a); i <= _n; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i >= _b; --i)
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define rep(i,n) FOR(i,0,(n)-1)
#define sum(c) (int)accumulate(all(c),0.)
#define VI vector <int>
#define ll long long
#define sqr(x) ((x)*(x))

#define MAX 100
using namespace std;



int main()
{
	

	ifstream in("input.in");
	ofstream out("magic.out");
	int t;
	in >> t;
	FOR(test,1,t)
	{
		int row[17][2] = {};
		int ans1,ans2,tmp;
		in >> ans1;
		rep(i,4)
			rep(j,4)			
		{
			in >> tmp;
			row[tmp][0] = i;
		}

		in >> ans2;
		rep(i,4)
			rep(j,4)			
		{
			in >> tmp;
			row[tmp][1] = i;
		}
		int res = 0;
		FOR(i,1,16)
			if(row[i][0] == ans1-1 && row[i][1] == ans2-1)
				if(res)
				{
					res = INF;
					break;
				}
				else res = i;
		out << "Case #"<< test << ": ";
		if(res == 0)
			out << "Volunteer cheated!" << endl;
		else if(res == INF)
			out << "Bad magician!" << endl;
		else out << res << endl;
			

	}
}

//*/