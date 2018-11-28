
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iostream>
#include <functional>
#include <time.h>
#include <cmath>
#include <deque>
 
using namespace std;
 
#define ll long long
#define mp make_pair
#define pb push_back
#define double long double
#define pii pair<int, int>
#define pll pair<ll, ll>
#define piii pair<int, pair<int, int> >
#define plll pair<ll, pair<ll, ll> >
#pragma comment(linker, "/STACK:36777216")
 
 

 
ll EPS = 1000000007;
double PI = 3.14159265358979323846;
const int MAXN = 1000010;
 
 


ll abss(ll h)
{
	return max(h, -h);
}
 
 
double fabss(double h)
{
	return max(h, -h);
}
 
ll ceill(ll x, ll y)
{
	if (x % y != 0)
	{
		return (x / y) + 1;
	}
	return x / y;
}
 
string itos(ll num)
{
	string str = "";
	while (num != 0)
	{
		str += ((num % 10) + '0');
		num /= 10;
	}
	reverse(str.begin(), str.end());
	return str;
}


ll n, m, k, r, t;

int a[MAXN];;
int d[1010][12];
int used[MAXN];





ll answer = EPS;


int findMaxIndex(int d)
{
	int index = 0;
	for (int i = 0; i < d; i++)
	{
		if (a[i] > a[index])
		{
			index = i;
		}
	}
	return index;
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> n;
	for (int q = 0; q < n; q++)
	{
		for (int i = 0; i < MAXN; i++)
		{
			a[i] = 0;
		}
		int d;
		cin >> d;
		int answer = 0;
		for (int i = 0; i < d; i++)
		{
			cin >> a[i];
			answer = max(answer, a[i]);
		}
		for (int i = 1; i <= 1000; i++)
		{
			int count = 0;
			for (int j = 0; j < d; j++)
			{
				if (a[j] <= i)
				{
					continue;
				}
				count += ceill(a[j] - i, i);
			}
			answer = min(answer, i + count);
		}
		cout << "Case #" << q + 1 << ": " << answer << endl;
	}
}