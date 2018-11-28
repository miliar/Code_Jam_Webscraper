//IN THE NAME OF GOD
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <fstream>
#include <utility>
#include <sstream>
#include <list>
#include <iomanip>
#include <functional>
#include <deque>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <complex>
#include <climits>
#include <cctype>
#include <cassert>
#include <bitset>
#include <limits>
#include <numeric>

//#pragma comment(linker, "/STACK:1024000000,1024000000")

using namespace std;

#define timestamp(x) printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
#define INF 100000000
#define pii pair < int , int >
#define MP make_pair
#define MOD 1000000007
#define EPS 1e-9
#define LL long long
#define MAXN 200000+10
#define bug cout<<"!!!!!!!!!!!!!!!!!";

int main()
{
	ios::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("i.txt", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t , tc = 1 ;
	double res, c, f, x , a , b , cook ;
	scanf("%d", &t);
	while (t--){
		cook = 2.;
		res = 0.;
		scanf("%lf %lf %lf", &c, &f, &x);
		while (1){
			a = x / cook ;
			b = (c / cook) + (x / (cook + f));
			if (b < a){
				res += c / cook;
				cook += f;
			}
			else{
				res += a;
				break;
			}
		}
		printf("Case #%d: %.7lf\n", tc++, res);
	}
	return 0;
}