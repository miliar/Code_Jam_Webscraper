/*
Author : OmarEl-Mohandes
PROG   : B
LANG   : C++
*/
#include <map>
#include <string>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <memory.h>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)m;i++)
#define REP(i,k,m) for(int i=k;i<(int)m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define oo ((int)1e9)
int compare(double d1, double d2) {
	if (fabs(d1 - d2) < 1e-9)
		return 0;
	if (d1 < d2)
		return -1;
	return 1;
}
int main()
{
	freopen("test.in" , "rt" , stdin);
	freopen("B.out" , "wt" , stdout);

	int t;
	cin >> t;
	rep(i , t){
		double c , f ,x;
		cin >> c >> f >> x;
		double ff = 2.0;
		double res = 0;
		while(1)
		{
			double tt = x / ff;
			double tf = c / ff;
			if(compare(tt , tf + (x / (ff + f))) <= 0){
				res += tt;
				break;
			}
			res += tf;
			ff += f;
		}
		printf("Case #%d: %.7lf\n" , i+1 , res);
	}
	return 0;
}

