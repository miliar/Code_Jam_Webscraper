#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <cassert>
using namespace std;
#define TR(i,v) 		for(__typeof((v).begin())i=(v).begin();i!=(v).end();++i)
#define DEBUG(x) 		cout << #x << " = "; cout << x << endl;
#define SIZE(p) 		(int)(p).size()
#define MP(a, b)		make_pair((a), (b))
#define ALL(p)			(p).begin(), (p).end()
#define rep(i, n)		for(int (i)=0; (i)<(int)(n); ++(i))
#define REP(i, a, n)	for(int (i)=(a); (i)<(int)(n); ++(i))
#define FOR(i, a, b)   	for(int (i)=(int)(a); (i)<=(int)(b); ++(i))
#define FORD(i, b, a)  	for(int (i)=(int)(b); (i)>=(int)(a); --(i)) 
typedef long long LL;
typedef pair<int, int> pii;
double C, F, X;
const double eps = 1e-6;
inline int cmp(double x, double y)
{
	return abs(x-y) < eps ? 0 : x < y ? -1 : 1;
}
int main(int argc, char const *argv[])
{
	#ifndef ONLINE_JUDGE
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    #endif
	// ios::sync_with_stdio(false);		cin.tie(0);
    int T;			scanf("%d", &T);
    FOR(cs, 1, T)
    {
    	scanf("%lf%lf%lf", &C, &F, &X);
    	double r = X/2;
    	double t = 0, inc = 2;
    	int cnt = 0;
    	while(1)
    	{
    		++cnt;    		
    		t += C/inc;
    		if(cmp(t, r) >= 0)		break;
    		inc += F;
    		double c = t + X/inc;
    		if(cmp(c, r) < 0)
    			r = c;
    	}
    	// DEBUG(cnt);
    	printf("Case #%d: %.12lf\n", cs, r);
    }
	return 0;
}