#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>
#include <vector>
#include <fstream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cmath>

using namespace std;
#define LL long long
#define FILES freopen("input.txt" ,"r", stdin); freopen("output.txt", "w", stdout);
#define FASTER ios::sync_with_stdio(0);

int main()
{
	FILES;
	FASTER;
	int T;
	cin >> T;
	string shLevel;
	for (int test = 1; test <= T; test++)
	{
		int maxS;
		cin >> maxS >> shLevel;
		int add = 0;
		int cnt = 0;
		for (int i = 0; i < shLevel.size(); i++)
		{
			if (shLevel[i] == '0') continue;

			if (cnt < i)
			{
				int dif = i - cnt;
				add += dif;
				cnt += dif;
			}

			cnt += shLevel[i] - 48;
		}
		cout << "Case #" << test << ": " << add << '\n';
	}
}