#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <stdio.h>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cstring>
#include <cmath>
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define eps 1e-9
#define PI acos(-1.0)
#define ll long long
#define ull unsigned long long
#define f0(i,n) for (i = 0; i < n; i++)
#define MOD 1000000007
using namespace std;
int i, j, n, m, k , t , test;
int p , r , s;

string go(char c , int lvl)
{
	string ret;
	if (lvl == n)
	{
		ret += c;
		return ret;
	}

	if (c == 'R')
	{
		string s1 = go('R' , lvl + 1);
		string s2 = go('S' , lvl + 1);
		if (s1 < s2)
			return s1 + s2;
		else
			return s2 + s1;
	} 

	if (c == 'S')
	{
		string s1 = go('S' , lvl + 1);
		string s2 = go('P' , lvl + 1);
		if (s1 < s2)
			return s1 + s2;
		else
			return s2 + s1;
	} 

	if (c == 'P')
	{
		string s1 = go('R' , lvl + 1);
		string s2 = go('P' , lvl + 1);
		if (s1 < s2)
			return s1 + s2;
		else
			return s2 + s1;
	} 

}

string ans;
int u[300];
void check(string t)
{
	int i;
	for (i = 0; i < 300; i++)
		u[i] = 0;
	for (i = 0; i < t.size(); i++)
	{
		u[t[i]]++;
	}

	if (u['R'] == r && u['S'] == s && u['P'] == p)
	{
		if (ans == "")
			ans = t;
		else
			ans = min(ans , t);
	}
}

int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	for (test = 1; test <= t; test++)
	{
		
		ans = "";
		cin>>n>>r>>p>>s;
		string s1 = go('R' , 0);
		string s2 = go('P' , 0);
		string s3 = go('S' , 0);
		check(s1);
		check(s2);
		check(s3);

		cout<<"Case #"<<test<<": ";
		if (ans == "")
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ans<<endl;
	}

	return 0;
}