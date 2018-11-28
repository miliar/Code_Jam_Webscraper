#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>
#define SI(x) scanf("%d" , &x)
#define SL(x) scanf("%lld" , &x)
#define SD(x) scanf("%lf" , &x)
#define SF(x) scanf("%f" , &x)
#define FI(i , s , e) for(i = s ; i < e ; i++)
#define FD(i , s , e) for(i = s ; i >= e ; i--)
#define PI(x) printf("%d\n" , x)
#define PL(x) printf("%lld\n" , x)
#define PD(x) printf("%lf\n" , x)
#define PF(x) printf("%f\n" , x)
#define VI vector<int>
#define VL vector<long long>
#define VVI vector<vector<int> >
#define VVL vector<vector<long long> >
#define priority_queue<int> PQI
#define priority_queue<long long> PQL
#define LL long long
#define N 1000000009
 
using namespace std;

int main()
{
	int t , p;
	double c , f , x , i , j , k;
	SI(t);
	p = 1;
	while(t--) {
		SD(c);
		SD(f);
		SD(x);
		k = 2.0;
		i = 0.0;
		while(x / k > ( (c / k) + (x / (k + f)) ) ){
			i += c / k;
			k += f;
		}
		i += x / k;
		printf("Case #%d: %.7lf\n" , p , i);
		p++;
	}
	return 0;
}