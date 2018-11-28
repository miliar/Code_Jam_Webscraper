#if !ONLINE_JUDGE
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <stack>
using namespace std;


int n;
vector <int> m;
long long mini;
void  get_minute(long long, long long);

bool canWork(long long);

int main()
{
#if !ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output1.out", "w", stdout);
#endif
	
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		int b;
		cin >> b >> n;
		m.resize(b);
		for (int i = 0; i < b; i++) cin >> m[i];
		long long maxi = 1;
		maxi <<= 62;
		mini = maxi + 1;
		get_minute(0, maxi);

		long long minute = mini;
	//	cout << minute;
		long long count = 0;
		for (int i = 0; i < b; i++)
		{
			count += (minute / m[i]);
			if (minute%m[i]>0) count++;
		}
		int ans = -1;
		for (int i = 0; i < b; i++)
		{
			if (minute%m[i] == 0)
			{
				count++;
				if (count == n) {ans = i + 1; break;}
			}
		}
		cout << "Case #" << z << ": " << ans << endl;
	}

	return 0;
}


void get_minute(long long  s, long long  e)
{
	if (s > e) return;
	long long mid = s + (e - s) / 2;
	if (canWork(mid))
	{
		mini = min(mid, mini);
		get_minute(s, mid - 1);
	}
	else
	{
		get_minute(mid + 1, e);
	}

}


bool canWork(long long minute)
{
	long long count = 0;
	for (int i = 0; i < m.size(); i++)
	{
		count += (minute / m[i]);
		count++;
		if (count >= n ) return true;
	}
	return false;
}