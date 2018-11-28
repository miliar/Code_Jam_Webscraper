//Created By Mayur Agarwal :)

#include <iostream>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <algorithm>
#include <map>
#include <iterator>
#include <functional>
#include <stack>
#include <queue>

#define ll long long
#define ind(a) scanf("%d",&a)
#define in(a) scanf("%lld",&a)
#define inc(a) scanf("%c",&a)
#define ins(a) scanf("%s",a)
#define pr(a) printf("%lld\n",a)
#define prc(a) printf("%c",a)
#define prs(a) printf("%s\n",a)
#define fori(I,N) for(ll I=0;I<N;I++)
#define forin(i,n) for(ll I=1;I<=N;I++)
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define ALL(X) (X).begin(), (X).end()
#define pi   acos(-1.0)
#define mod 1000000007
#define SIZE 200010

using namespace std;
typedef pair<ll, ll>pll;
int bin[30];
int k;
ll ar[20];
std::vector<ll> vec[30];
void binary(ll n)
{
	if (n > 1)
		binary(n / 2);
	bin[k++] = n % 2;
}
inline int isprime(ll num)
{
	for (int i = 2, k = sqrt(num) * 1.0; i <= k; i++)
	{
		if (num % i == 0)
		{
			return i;
		}
	}
	return 0;
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0); cin.tie(0);
	int t;
	ind(t);
	for (int xx = 1; xx <= t; xx++)
	{
		int n, m;
		ind(n);
		ind(m);
		int x = 0;
		bool glob_flag = 0;
		for (int mask = 0; mask < (1 << 16); mask++)
		{
			//cout << mask << endl;
			//int i = 0, j = 5;
			if ((mask & (1 << 0)) && (mask & (1 << 15)))
			{
				//cout << "TT" << endl;
				k = 0;
				int p = 0;
				bool flag = 0;
				binary(mask);
				for (int j = 2; j <= 10; j++)
				{
					ll temp = 1;
					ll num = 0;
					for (int i = k - 1; i >= 0; i--)
					{
						num += bin[i] * temp;
						temp *= j;
					}
					ll val = isprime(num);

					if (val != 0)
					{
						ar[p++] = val;
					}
					else
					{
						flag = 1;
						break;
					}
					if (j == 10 && p == 9)
					{
						ar[p++] = num;
					}
				}
				if (!flag)
				{
					x++;
					int poo = x;
					vec[poo].push_back(ar[p - 1]);
					for (int i = 0; i < p - 1; i++)
					{
						vec[poo].push_back(ar[i]);
					}
					if (poo >= 50)
					{
						glob_flag = 1;
						break;
					}
				}
				MS0(ar);
				MS0(bin);
			}
			if (glob_flag == 1)
			{
				break;
			}
		}
		cout << "Case #" << xx << ": \n";
		for (int i = 1; i <= 50; i++)
		{
			for (int j = 0; j < vec[i].size(); j++)
			{
				cout << vec[i][j] << " ";
			}
			cout << endl;
		}

	}
	return 0;
}