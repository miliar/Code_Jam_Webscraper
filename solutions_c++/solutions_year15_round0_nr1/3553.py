
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





int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> n;
	string str;
	for (int q = 0; q < n; q++)
	{
		cin >> m;
		cin >> str;
		ll answer = 0;
		ll count = 0;
		for (int i = 0; i < str.size(); i++)
		{
			if (count >= i)
			{
				count += (ll)(str[i] - '0');
			}
			else
			{
				ll q = i - count;
				answer += q;
				count += q;
				count += (ll)(str[i] - '0');
			}
		}
		cout << "Case #" << q + 1 << ": " << answer << endl;
	}
}