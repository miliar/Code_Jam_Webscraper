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
#include <string.h>
#include <cstring>
#define oo (int)1e9
#define fill( a , v ) memset( a , v , sizeof (a) )
#define bits( x ) __builtin_popcount( x )
#define gcd( a , b ) __gcd( a, b )
#define lcm( a , b ) (a/gcd( a, b ) ) * b
#define s(n)scanf( "%d" , &n )
#define add push_back
const int mxn = 1000000 + 10;
typedef long long ll;
#define pii pair<double,double>
using namespace std;
int cs, T;
int a[mxn], N;
string s;


int solve() {

	if(N == 0) {
		int required = a[0] == 0 ? 1 : 0;
		return required ;
	}


	int up = a[0];
	int cur = 1;
	int required = 0;
	while(cur <= N) {
		// printf("%d %d %d\n", up, cur, required);
		if(a[cur] == 0) {cur++; continue;}
		if(cur <= up) {
			up += a[cur];
			cur++;
		}
		else {
			required += cur - up;
			up += a[cur] + cur - up;
			cur++;
		}
	}
	// cout << required << endl;
	return required;
}

int main() {
	int first, second;
	s(T);

	while(T--) {
		fill(a, 0);
		cin >> N >> s;

		for(int i=0;i<s.size();i++)
			a[i] = s[i] - '0';

		printf("Case #%d: %d\n", ++cs, solve());
	}
}