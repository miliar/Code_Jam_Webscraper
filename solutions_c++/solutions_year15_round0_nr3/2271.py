/*
*************************************************************************
* $ Author : honeyslawyer   $
* $ Name   : shashank gupta $
*************************************************************************
*
* Copyright 2014 @ honeyslawyer and shashank gupta
*
************************************************************************/
#include<cstdio>
#include<iostream>
#include<cmath>
#include<conio.h>
#include<cstring>
#include<ctype.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<map>
#include<queue>
#include<stack>
#include<set>
#include<string>
#include<climits>

#define mod 1000000007
#define ll long long

using namespace std;
ll gcd(ll a,ll b) {if(b==0) return a; return gcd(b,a%b);}

ll power(ll b,ll exp,ll m)
 {ll ans=1;
  b%=m;
  while(exp)
   {if(exp&1)
     ans=(ans*b)%m;
    exp>>=1;
	b=(b*b)%m;
   }
  return ans;
 }

map<pair<int,int> ,int> mp;
int a[4][4] = { { 1, 2, 3, 4 }, { 2, -1, 4, -3 }, { 3, -4, -1, 2 }, { 4, 3, -2, -1 } };
int b[4][4] = { { 1, -2, -3, -4 }, { 2, 1, 4, -3 }, { 3, -4, 1, 2 }, { 4, 3, -2, 1 } };
int mul(int m1, int m2)
{
	int tmp = a[abs(m1) - 1][abs(m2) - 1];
	if (m1 / abs(m1) == m2 / abs(m2))
		return tmp;
	else
		return -tmp;
}
int divv(int m1, int m2)
{
	int tmp = b[abs(m1) - 1][abs(m2) - 1];
	if (m1 / abs(m1) == m2 / abs(m2))
		return tmp;
	else
		return -tmp;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
	int i, j, k, t, n, m, x, l, y;
	cin >> t;
	for (x = 1; x <= t; ++x)
	{
		cin >> l >> y;
		string s, p;
		cin >> s;
		for (i = 0; i < s.size(); ++i)
			s[i] = s[i] - 'i' + '2';
		//cout << s << endl;
		for (i = 0; i < y; ++i)
			p += s;
		//cout << p << endl;
		int flag = 0;
		int c1, c2, c3;
		c1 = p[0] - '0';
		c2 = p[1] - '0';
		c3 = p[2] - '0';
		for (k = 3; k< p.size(); ++k)
			c3 = mul(c3, p[k] - '0');
		for (i = 1; i < p.size()-1 && flag==0; ++i)
		{
			if (i>1)
			{
				c1 = mul(c1, p[i - 1] - '0');
				c2 = p[i] - '0';
				c3 = divv(c3, p[i] - '0');
			}
			int ci3 = c3;
			for (j = i+1; j < p.size() && flag==0; ++j)
			{
				if (j>i + 1)
				{
					ci3 = divv(ci3, p[j - 1] - '0');
					c2 = mul(c2, p[j - 1] - '0');
				}
				if (c1 == 2 && c2 == 3 && ci3 == 4)
				{
					flag = 1;
				}
			}
			//if (i > 500)
			//	cout << "yo";
		}
		cout << "Case #" << x << ": ";
		if (flag == 0)
			cout << "NO\n";
		else
			cout << "YES\n";
	}
	getch();
	return 0;
}