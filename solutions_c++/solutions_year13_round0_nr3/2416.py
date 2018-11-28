//Solution by Zhusupov Nurlan
#include <iostream>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <stack>
#include <queue>
#include <ctime>

using namespace std;

typedef long long LL;
typedef map<string , int> MSI;
typedef vector<int> VI;

#define pb(x) push_back(x)
#define sqr(x) ((x) * (x))
#define F first
#define S second
#define SZ(t) ((int) t.size())
#define len(t) ((int) t.length())
#define base 10
#define fname ""
#define sz 1000 * 10001
#define EPS (1e-8)
#define INF ((int)1e9 + 9)
#define write(xx) printf("%d" , xx);
#define readln(xx) getline(cin , xx)
#define read(xx) scanf("%d" , &xx)
#define for(xx1 , yy1 , zz1) for(int zz1 = xx1 ; zz1 <= yy1 ; zz1++)

const double PI  = acos(-1.0);

int k, c1[sz], c2[sz], d[sz], t;
LL a, b;

bool check(LL x)
{	
	k = 0;
	while (x)
	{
		k++;
		c1[k] = c2[k] = x % 10;
		x /= 10;
	}
	reverse(c2 + 1, c2 + k + 1);

	for (1, k, i)
		if (c1[i] != c2[i])
			return false;
   	return true;
}

int get(LL x)
{
	return d[int(sqrt(x))];
}

int main(){
	freopen(fname"in", "r", stdin);
	freopen(fname"out", "w", stdout);

	cin >> t;
	for (1, 10000000, i)
	{
		if (check(i) && check((LL)i * i))
			d[i]++;
	   	d[i] += d[i - 1];
	}


	for (1, t, test)
	{
		cout << "Case #" << test << ": ";
		cin >> a >> b;
		cout << get(b) - get(a - 1) << endl;
	}

    	return 0;
}
