#define _CRT_SECURE_NO_WARNINGS
//#include <bits/stdc++.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<unordered_map>
#include<queue>
#include<stack>
#include<iterator>
#include<cmath>
#include<string>
#include<sstream>
#include<cstring>
#include<ctype.h>
#include<iomanip>
#include<bitset>
#include<stdio.h>
#include<fstream>
#include<regex>
#include<stdlib.h>
#include<math.h>

using namespace std;

#define READ(s)   freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

vector<int> arr(10);

int fn(int i, vector<int> a)
{
	if (i == 1) return 1;
	int n = 999999;
	for (int j = 1; j < i; j++)
	{
		a[j] = a[j] + a[i];
		a[i - j] = a[i - j] + a[i];
		for (int k = i - 1; k > 0; k--)
			if (a[k])
			{
				n = min(n, fn(k, a));
				break;
			}
		a[j] = a[j] - a[i];
		a[i - j] = a[i - j] - a[i];
	}
	int rm = min(n + a[i], i);
	for (int j = 0; j < i; j++)
		a[j] = a[j + 1];
	for (int j = i - 1; j > 0; j--)
		if (a[j] > 0)
		{
			rm = min(rm, fn(j, a) + 1);
			break;
		}
	return rm;
}

int main()
{
	READ("B-small-attempt10.txt");WRITE("output.txt");
	int T; cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int D; cin >> D;
		int m = 0;
		for (int j = 0; j < 10; j++) arr[j] = 0;
		for (int j = 0; j < D; j++)
		{
			int a; cin >> a;
			arr[a]++;
			if (a > m) m = a;
		}
		int answer = fn(m, arr);
		printf("Case #%d: %d\n", i, answer);
	}
}