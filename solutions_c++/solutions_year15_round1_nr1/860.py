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

vector <int> m;
void get_min(int, int);
bool canWork(int);
int mini; 

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
		int n;
		cin >> n;
		m.resize(n);
		for (int i = 0; i < n; i++) cin >> m[i];
		int y = 0;
		int maxi = 0;
		for (int i = 1; i < n; i++)
		{
			if (m[i] < m[i - 1])
			{
				y += (m[i - 1] - m[i]);
				maxi = max(maxi, m[i - 1] - m[i]);
			}
		}
		/*mini = 10003;
		get_min(0,10002);
		int rate = mini;
		int f = 0;
		for (int i = 0; i < n - 1; i++)
		{
			f += min(10 * rate, m[i]);
		}*/
		int f = 0;
		for (int i = 0; i < n - 1; i++)
		{
			f += min(maxi, m[i]);
		}

		cout << "Case #" << z << ": " << y << " " << f << endl;
	}

	return 0;
}


void get_min(int s, int e)
{
	if (s > e) return;
	int mid = s + (e - s) / 2;
	if (canWork(mid))
	{
		mini = min(mid, mini);
		get_min(s, mid - 1);
	}
	else
	{
		get_min(mid + 1, e);
	}

}

bool canWork(int rate)
{
	for (int i = 1; i < m.size(); i++)
	{
		if (m[i] < m[i - 1])
		{
			if (m[i - 1] - m[i] > rate * 10) return false;
		}
	}
	return true;
}