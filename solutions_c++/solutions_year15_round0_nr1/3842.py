#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <fstream>
#include <string>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <queue>
#include <time.h>
#include <stdio.h>
#include <list>
#include <stdlib.h>
#include <string.h>
#include <list>
#include <functional>
#include <random>
using namespace std;
//#define JUDJE 1488

#ifndef JUDJE

ifstream in("aaa.in");
ofstream out("output.txt");
#define cin in
#define cout out

#endif

#define ll long long
#define MOD 1000000007
#define mp(a, b) make_pair(a, b)
#define PI 3.1415926535
#define EPS 0.00000001
#define pii pair<int, int>
#define INF 1000000000

int main()
{
	int t;
	cin >> t;
	for(int ii = 1; ii <= t; ++ii)
	{
		int n;
		cin >> n;
		string s;
		cin >> s;
		int ans = 0;
		int curMan = s[0] - '0';
		for(int i = 1; i < s.size(); ++i)
		{
			if(curMan < i)
			{
				++ans;
				curMan++;
			}
			curMan += s[i]-'0';
		}
		cout << "Case #" << ii << ": " << ans << "\n";
	}

}

 
/*

10 8
-2 9 3 6 3 8 -1 10 -6 7
*/

