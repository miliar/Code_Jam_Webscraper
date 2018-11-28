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

//	srand(time(NULL));
//	cout<<fixed<<setprecision(3)<<"\nExecution time="<<clock()/1000.0<<endl;
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);

int n, m, i, j, k, q, s, w, v, ans;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> w;
	while (w--)
	{
		v++;
		string t;
		cin >> n >> t;

		q = 0;
		int cur = t[0] - '0';

		for (i = 1; i <= n; i++)
		{
			if (t[i]!='0' && cur <= i)
			{
				q += i - cur;
				cur += i - cur;
			}
			cur += t[i] - '0';
		}
		printf("Case #%d: %d\n", v, q);
	}
	return 0;
}




