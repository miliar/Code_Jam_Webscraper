#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <stdio.h>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cstring>
#include <cmath>
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define eps 1e-9
#define PI acos(-1.0)
#define ll long long
#define ull unsigned long long
#define f0(i,n) for (i = 0; i < n; i++)

using namespace std;

ll n, i, j, k, m;
int u[10];

int main() 
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		string s;
		cin >> s;

		string t;
		t += s[0];
		for (i = 1; i < s.size(); i++)
			if (s[i] != s[i - 1])
				t += s[i];


		if (t[t.size() - 1] == '+')
			t.erase(t.size() - 1, 1);
		
		

		cout << "Case #" << tt << ": ";
		cout << t.size() << endl;
	}
	return 0;
}