#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>

typedef long long int lli;
typedef long int li;

#define F(i, n) for(i = 0;i < n; ++i)
#define FI(i, st, ft) for(i = st;i <= ft; ++i)
#define pb(a, b) a.push_back(b)

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	li k, t;
	cin >> t;
	F(k, t){
		li cnt = 1;
		double c, f, x, cur, ex, temp;
		cin >> c >> f >> x;
		double rate = 2.0000;
		cur = x / rate;
		ex = c / rate + x / (rate + f) ;
		rate += f;
		temp = cur;
		while(ex < cur){
			++cnt;
			cur =  ex;
			ex += (c / rate) + x / (rate + f) - x / (rate);
			rate += f;
			temp = cur;
		}
		printf("Case #%ld: %0.7lf\n",k + 1, temp);
	}
	return 0;
}
