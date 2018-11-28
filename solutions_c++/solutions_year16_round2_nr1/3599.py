/*
* @problem: 1BA
*/
#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <string.h>
#include <set>
#include <map>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <functional>
#include <bitset>
#include <iomanip>
#define ll long long
#define pi acos(-1.0)
#define pb push_back
#define MS0(ar) memset(ar,0,sizeof ar)
#define MS1(ar) memset(ar,-1,sizeof ar)
#define ff first
#define ss second
#define pii pair<int,int>
#define pll pair<ll,ll>
#define ind(a) scanf("%d",&a)
#define inf(a) scanf("%lf",&a)
#define inl(a) scanf("%lld",&a)
#define ins(a) scanf("%s",a)
#define pd(a) printf("%d\n",a)
#define pl(a) printf("%lld\n",a);
#define bitcnt(x) __builtin_popcountll(x)
using namespace std;
int cnt[26], req[26];
int main()
{

	ios_base::sync_with_stdio(0);
	cin.tie(0);
#ifndef ONLINE_JUDGE
	freopen("../input.txt", "r", stdin);
	freopen("../output.txt","w",stdout);
#endif
	int t;
	string s;
	string d[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	cin >> t;
	for (int k = 1; k <= t; ++k)
	{
		cin >> s;
		MS0(cnt);
		for (int i = 0; i < s.length(); ++i)
			cnt[s[i] - 65]++;
		string str = "";
		for (int i = 9; i >=0; --i)
		{
			bool is_pos = true;
			while (is_pos)
			{
				//cout<<d[i]<<endl;
				MS0(req);
				for (int j = 0; j < d[i].length(); ++j)
				{
					req[d[i][j] - 65]++;
				}
				for (int j = 0; j <= 25; ++j)
				{
					if ((cnt[j] < req[j]))
						is_pos = false;
				}
				if (is_pos)
				{
					//cout << d[i] << endl;
					str += char(i + 48);
					for (int j = 0; j <= 25; ++j)
						cnt[j] -= req[j];

				}
				else
					break;
			}
		}
		int flag=1;
		for(int i=0;i<=25;++i)
		{
			if(cnt[i]!=0)
				flag=0;
		}
		if(flag)
		{
			sort(str.begin(),str.end());
		cout << "Case #" << k << ": " << str << endl;
		continue;
		}
		MS0(cnt);
		for (int i = 0; i < s.length(); ++i)
			cnt[s[i] - 65]++;
		str = "";
		for (int i = 0; i<=9; ++i)
		{
			bool is_pos = true;
			while (is_pos)
			{
				//cout<<d[i]<<endl;
				MS0(req);
				for (int j = 0; j < d[i].length(); ++j)
				{
					req[d[i][j] - 65]++;
				}
				for (int j = 0; j <= 25; ++j)
				{
					if ((cnt[j] < req[j]))
						is_pos = false;
				}
				if (is_pos)
				{
					//cout << d[i] << endl;
					str += char(i + 48);
					for (int j = 0; j <= 25; ++j)
						cnt[j] -= req[j];

				}
				else
					break;
			}
		}
		sort(str.begin(),str.end());
		cout << "Case #" << k << ": " << str << endl;

	}
	return 0;
}