#include"stdafx.h"
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<queue>
#include<math.h>
#include<vector>
#include<deque>
#include<stack>
#include<set>
#include<sstream>
#include<algorithm>

using namespace std;


#pragma warning(disable : 4996)
#define mp(a,b) (make_pair(a,b))
#define mms memset
#define LL long long
#define y1 y1111
#define eps 1e-9
#define y2 y2222
#define LINF LLONG_MAX
#define INF 1000000000
#define PI 3.14159265359
#define mod 1000000007
#define x1 x1111
#define x2 x2222
#define pow10 pppp

int main(void)
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	double c, f, x,ans,sp;

	cin >> t;
	for (int i = 0; i < t; i++)
	{
		ans = 0;
		sp = 2;
		cin >> c >> f >> x;
		while (true)
		{
			if (x / (sp)>(c / sp + x / (sp + f)))
			{
				ans += c / sp;
				sp += f;
			}
			else
			{
				printf("Case #%i: %.6Lf\n", i+1, ans + x / sp);
				break;
			}
		}
	}
	
}
