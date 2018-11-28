#define _CRT_SECURE_NO_WARNINGS
 
#include <iostream>
#include <functional>
#include <vector>
#include <queue> 
#include <string>
#include <math.h>
#include <algorithm>
#include <limits>
#include <set>
#include <map>
 
#define sqr(x) ((x) * (x))
#define eps 0.00000001
 
using namespace std;

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
	int t;
	cin >> t;
	string str;
	int len;
	for (int i = 0; i < t; i++)
	{
		int ans = 0, sum = 0;
		cin >> len;
		cin >> str;
		for (int j = 0; j < len + 1; j++)
		{
			if (sum < j)
			{
				ans += j - sum;
				sum = j;
			}
			sum += str[j] - '0';
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
}