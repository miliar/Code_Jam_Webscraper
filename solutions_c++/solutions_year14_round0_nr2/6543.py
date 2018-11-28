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


double c,f,x;


int main()
{
	freopen("input.in","rt",stdin); 
    freopen("output.out","wt",stdout); 
	int t;
	cin >> t;
	FOR(test,1,t)
	{
		cin >> c >> f >> x;

		double time = 0.;
		double p = 2.;
		double res = x/p;

		for(int i = 1 ; ; ++i)
		{
			time += c/p;
			p +=f;
			double new_res = time + x/p;
			if( new_res > res ) break;
			else
				res = new_res;
		}
		cout <<"Case #"<<test << ": " << fixed << setprecision(7) << res << endl; 
	}
	return 0;
	
}

//*/