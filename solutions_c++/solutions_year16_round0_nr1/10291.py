#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<string.h>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include <stack>
//#include<bits/stdc++.h>
#define MAXN 1000005
#define MAXV 10005
#define mod 100000007
#define ssp system("pause")

using namespace std;
typedef long long ll;


int main()
{
	int T;
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ll cot = 0;
	ll n;
	cin >> T;
	while (T--)
	{
		printf("Case #%lld: ", ++cot);
		
		//int show[10] = { 0 };
		cin >> n;
		//if (!(n % 1)){ cout << "impossible\n"; continue; }
		int cot = 10;
		ll ans = 0;
		ll show[10] = { 0 };
		if (n == 0){
			cout << "INSOMNIA\n"; continue;
		}
		for (ll i = 1; i <= 10000000000000; i++)
		{
			ll te=i*n;
			ll temp = te;
			while (temp)
			{
				if (!show[temp % 10])cot--;
				show[temp % 10]++;
				temp /= 10;
			}
			if (cot==0)
			{
				ans = i*n;
				goto there;
			}
		}
	there:
		if (ans)
			cout << ans << endl;
		else cout << "INSOMNIA\n";
	}
	return 0;
}