#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <ctime>
using namespace std;

#define inf 2147483647
#define eps 0.0000000001
#define e  2.718281828459
#define pi 3.1415926535897932
#define mod 1000000007

#define LL long long
#define ULL unsigned long long
#define LD long double
#define ULD unsigned long double
#define topcoder classname

const int N = 100005;

//	srand(time(NULL));
//	cout<<fixed<<setprecision(3)<<"\nExecution time="<<clock()/1000.0<<endl;
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);

int n, m, i, j, k, q, s, w, v, ans;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	cin >> w;
	for (int Tc = 1; Tc <= w; Tc++)
	{
		string t;
		cin >> t;
		char best = t[0];
		string p;
		p = t[0];

		for (int i = 1; i < t.length(); i++)
		{
			if (t[i] >= best) {
				best = t[i];
				p = t[i] + p;
			}
			else
				p = p + t[i];
		}

		printf("Case #%d: ", Tc);
		cout << p << "\n";
	}
	return 0;
}