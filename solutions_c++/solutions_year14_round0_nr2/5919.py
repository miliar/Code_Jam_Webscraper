#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <iterator>
#include <utility>
#include <list>
#include <stack>
#include <iomanip>
//#include <bitset>

#define MAX_INT 2147483647
#define MAX_LONG 9223372036854775807ll
#define MAX_ULONG 18446744073709551615ull
#define MAX_DBL 1.7976931348623158e+308
#define EPS 1e-9;

#define INF 1000000000
//22:01
using namespace std;
 
int t, i, j;
double c, f, x, ant, act, sum, con;

int main() {
	
	scanf("%d", &t);
	
	for (i=1; i<=t; i++) {
		
		scanf("%lf %lf %lf", &c, &f, &x);
		
		ant = MAX_DBL;
		act = 0.0;
		sum = 2.0;
		con = 0.0;
		
		while (ant > act) {
			ant = con + (x / sum);
			
			con += c / sum;
			sum = sum + f;
			act = con + (x / sum);
		}
		
		printf("Case #%d: %.7lf\n", i, ant);
		
	}
	
	
	return 0;
}