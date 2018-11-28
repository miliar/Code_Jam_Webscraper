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

	int t , x;
	SI(t);

	FI(x , 1 , t + 1) {
		
		int a;
		int b;
		int k;
		SI(a);
		SI(b);
		SI(k);
		if ( b > a ) {
			int t = b;
			b = a;
			a = t;
		}

		int ctr = 0;
		for ( int i = 0; i < a; i++) { 
			for ( int j = 0; j < b ; j++ ) {
				if ( (i&j) < k ) {
					ctr++;
					if ( i != j ) {
					//	ctr++;
					//	cout << j << "    " << i << endl;
						
					}
				//	cout << i << "    " << j << endl;
				}
			}
		}

		cout << "Case #" << x <<": " << ctr << endl;
	}

	return 0;
}
