#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <climits>
#include <cctype>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <deque>
#include <queue>
#include <stack>
#include <iomanip>
#include <complex>
#include <list>
#include <bitset>
#include <fstream>
#include <limits>
#include <memory.h>
#include<windows.h>
#include<iterator>
//#include<bits/stdc++.h>

using namespace std;

#define loop(i,j,n) for(int i=(j); i<(n);i++)
#define ll long long
#define all(x) x.begin(),x.end()
#define SZ(x) ((int)((x).size()))
#define PB push_back
#define VI vector<int>
#define LLVI vector<long long int>
#define VS vector<string>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int main()
{
	READ("B-large.in");
	WRITE("B-large.out");

	long double c, a, b, l, f, n;
	long int t, k;
	cin >> t;
	for (k = 0; k<t; k++)
	{
		cin >> c >> f >> l;
		b = l / 2.0 + 1;
		a = l / 2.0;
		n = 0.0;
		while (b>a)
		{
			if (a>(a - (l / (2 + (n*f))) + (c / (2 + n*f)) + l / (2 + (n + 1)*f)))
			{
				b = a;
				a = a - (l / (2 + (n*f))) + (c / (2 + n*f)) + l / (2 + (n + 1)*f);
			}
			else
				break;
			n++;
		}
		cout << fixed << setprecision ( 7 ) ;
		cout << "Case #" << k + 1 << ": " << fixed << a << "\n";

	}
//	system ("pause");
}
