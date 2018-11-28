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
#define sz 111
#define EPS (1e-8)
#define INF ((int)1e9 + 9)
#define write(xx) printf("%d" , xx);
#define readln(xx) getline(cin , xx)
#define read(xx) scanf("%d" , &xx)
#define for(xx1 , yy1 , zz1) for(int zz1 = xx1 ; zz1 <= yy1 ; zz1++)

const double PI  = acos(-1.0);

int n, m, t, a[sz][sz], r[3][sz][sz], c[3][sz][sz];
bool f;

int main(){
	freopen(fname"in", "r", stdin);
	freopen(fname"out", "w", stdout);

	cin >> t;

	for (1, t, test)
	{
		cin >> n >> m;

		cout << "Case #" << test << ": ";
		for (1, n, i)
			for (1, m, j)
				cin >> a[i][j];
	  	for (1, n, i)
	  	{
	  		r[0][i][0] = a[i][1];
	  		r[1][i][m + 1] = a[i][m];
	  		for (1, m, j)
	  		{
	  			r[0][i][j] = max(r[0][i][j - 1], a[i][j]);
	  			r[1][i][m - j + 1] = max(r[1][i][m - j + 2], a[i][m - j + 1]);
	  		}
	  	}
	  	for (1, m, j)
	  	{
	  		c[0][0][j] = a[1][j];
	  		c[1][n + 1][j] = a[n][j];
	  		for (1, n, i)
	  		{
	  			c[0][i][j] = max(c[0][i - 1][j], a[i][j]);
	  			c[1][n - i + 1][j] = max(c[1][n - i + 2][j], a[i][j]);	
	  		}
	  	}

	  	f = true;
	  	for (1, n, i)
	  		for (1, m, j)
	  			if ((r[0][i][j] != a[i][j] || r[1][i][j] != a[i][j]) && (c[0][i][j] != a[i][j] || c[1][i][j] != a[i][j]))
	  				f = false;
	 	if (f)
	 		cout << "YES";
	   	else
	   		cout << "NO";
	   	cout << endl;
		
	}

    	return 0;
}
