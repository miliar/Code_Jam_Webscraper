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
#include <ctime>
#include <stack>
using namespace std;

#define inf 2147483647
#define eps 0.0000000000001
#define pi 3.1415926535897932
#define mod 1000000007
#define LL long long
#define ULL unsigned long long
#define LD long double
#define ULD unsigned long double

const int N = 100005;

//	prLLf("Case #%d: ", v);
//	srand(time(NULL));
//	cout<<fixed<<setprecision(3)<<"\nExecution time="<<clock()/1000.0<<endl;
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);

LL n, m, i, j, k, q, s, w, v, ans;

int main()
{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	cin >> w;
	string t = "GABRIEL";
	string p = "RICHARD";
	while (w--)
	{
		v++;
		int x, y;
		cin >> n >> x >> y;
		if (n == 1 || (n == 2 && (x*y) % 2 == 0))
		{
			printf("Case #%d: ", v);
			cout << t << endl;
			continue;
		}
		if (n == 3 && (x*y) % 3 == 0 && min(x, y) != 1)
		{
			printf("Case #%d: ", v);
			cout << t << endl;
			continue;
		}
		if (n == 4 && (x + y == 7 || x + y == 8))
		{
			printf("Case #%d: ", v);
			cout << t << endl;
			continue;
		}

		printf("Case #%d: ", v);
		cout << p << endl;
	}
	return 0;
}

		

