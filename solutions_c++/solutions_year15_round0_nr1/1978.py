#define _CRT_SECURE_NO_WARNINGS
#include <unordered_set>
#include <functional>
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <bitset>
#include <string>
#include <cstdio>
#include <complex>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
using namespace std;



int main()
{
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif 
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n;  string s; cin >> n >> s;
		int ans = 0, sum = 0;
		for (int i = 0; i < n + 1; i++)
		{
			if (sum < i)
			{
				ans += i - sum;
				sum = i;
			}
			sum += s[i] - '0';
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
}