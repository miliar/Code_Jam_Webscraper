#include <iostream>
#include <stdio.h>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <sstream>
#include <cmath>
#define ull unsigned long long int
#define ll long long
#define Max(a,b) a >b ? a :b
#define S(n) scanf("%d",&n)
#define Sl(n) scanf("%ld",&n)
#define Sll(n) scanf("%lld",&n)
#define li long int
using namespace std;
int main()
{
	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	int k;
	cin >> t;
	for(k = 1; k <= t; k++) {
		double c,f,x;
		cin >> c >> f >> x;
		double ti = 0.0;
		double l1 = 0.0,l2;
		double r = 2.0;
		while(1) {
			l1 = c/ r + x / (r + f);
			l2 = x / r;
			if(l2 <= l1)  {
				ti  = ti + l2;
				break;
			} else {
				ti = ti + c/r;
				r = r + f;
			}
		}
		cout << "Case #" << k <<": ";
		printf("%0.7Lf\n",ti);
		
	}
	return 0;
}

