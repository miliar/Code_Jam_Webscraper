//#pragma comment(linker, "/STACK:836777216")

#define INF (long long)1e18
#define EPS 1e-15
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
#include <memory.h>

using namespace std;

int T;
int n;
string tmp_s;
char arr[100][101];
string min_string = "";
string strings[100];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cin >> T;
	for (int test = 1; test <= T; test++) 
	{
		min_string = "";
		cin >> n;

		int max_s = 0, min_s = INF;

		int bear[100][100];
		for (int i = 0; i < n; i++) 
		{
			for (int j = 0; j < 100; j++) 
			{
				bear[i][j] = 0;
			}
		}

		for (int i = 0; i < n; i++) 
		{
			cin >> tmp_s;
			strings[i] = tmp_s;
			if (max_s < tmp_s.length()) max_s = tmp_s.length();
			if (min_s > tmp_s.length()) min_s = tmp_s.length();
			if (min_string == "" || min_string.length() > tmp_s.length()) min_string = tmp_s;
			char curr_ch = '\0';
			int ind = 0;
			for (int j = 0; j < tmp_s.length(); j++) 
			{
				if (tmp_s[j] != curr_ch) 
				{
					arr[i][ind++] = tmp_s[j];
					curr_ch = tmp_s[j];
				}
			}
			arr[i][ind] = '\0';
		}
		bool ans = true;
		int main_ans = 0;
		for (int i = 0; i < n; i++) 
		{
			if (strcmp(arr[0], arr[i]) != 0) 
			{
				ans = false;
				break;
			}			
		}
		if (ans) 
		{
			int ind = -1;
			for (int i = 0 ; i < n; i++) 
			{
				char curr_ch = '\0';
				ind = -1;
				for (int j = 0; j < strings[i].length(); j++) 
				{
					if (strings[i][j] != curr_ch) 
					{
						ind++;
						bear[i][ind] =1;
						curr_ch = strings[i][j];
					} else 
					{
						bear[i][ind] ++;
					}
				}
			}
			int qqq = ind + 1;
			int avgs[100];

			for (int i = 0; i < 100; i++) avgs[i] = 0;
			for (int j = 0; j < qqq; j++) 
			{
				int sum = 0;
				for (int i = 0; i < n; i++) 
				{
					sum += bear[i][j];
				}
				avgs[j] = sum / n;
			}
			for (int j = 0; j < qqq; j++) 
			{
				for (int i = 0; i < n; i++) 
				{
					main_ans += abs(bear[i][j] - avgs[j]);
				}
			}
			cout << "Case #" << test << ": " << main_ans << '\n';
		} else 
		{
			cout << "Case #" << test << ": " << "Fegla Won" << '\n';
		}		
	}
	return 0;
}