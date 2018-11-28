#define _CRT_SECURE_NO_WARNINGS
//#define _USE_MATH_DEFINES

#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <math.h>
#include <vector>
#include <fstream>
#include <stack>
#include <ctime>
#include <map>
#include <list>
#include <cstdio>
#include <functional>
#include <bitset>
#include <set>
#include <limits.h>
#include <functional> 
#include <cctype>
#include <locale>
#include <queue>

using namespace std;

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
#define scani(s) scanf("%d", &s)
#define scanii(s, t) scanf("%d%d", &s, &t)

#define epsilon 1e-5
#define D_MAX 1e200
#define sec second.first
#define third second.second
#define INF 1000000000
#define gcd3(a, b, c) gcd(a, gcd(b, c))

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, bool> pib;
typedef pair<int, pair<int, int> > tiii;
typedef pair<ll, pair<ll, ll> > tlll;
typedef vector<int> vi;
typedef vector<vi> vii;

typedef long long ll;

ll gcd(ll a, ll b) { return (b == 0 ? a : gcd(b, a % b)); }
ll pw(ll b, ll e, ll m) { ll r = 1; b = b % m; while (e > 0){ if (e & 1)r = (r * b) % m; e >>= 1; b = (b * b) % m; }return r; }

#define MOD 1000000007
int arr[30];
int ans[10];
int main()
{
#ifndef ONLINE_JUDGE
	READ("in.txt");
	WRITE("out.txt");
#endif
	int t;
	cin >> t;
	string s;
	for (int z = 1; z <= t; z++)
	{
		if (z == 77)
			z = 77;
		memset(arr, 0, sizeof arr);
		memset(ans, 0, sizeof ans);
		cin >> s;
		for (int i = 0; i < s.size(); i++)
		{
			arr[s[i] - 'A']++;
		}
		ans[0] = arr['Z' - 'A'];
		arr['Z' - 'A'] = 0;
		arr['E' - 'A'] -= ans[0];
		arr['R' - 'A'] -= ans[0];
		arr['O' - 'A'] -= ans[0];

		ans[8] = arr['G' - 'A'];
		arr['E' - 'A'] -= ans[8];
		arr['I' - 'A'] -= ans[8];
		arr['G' - 'A'] -= ans[8];
		arr['H' - 'A'] -= ans[8];
		arr['T' - 'A'] -= ans[8];

		ans[6] = arr['X' - 'A'];
		arr['S' - 'A'] -= ans[6];
		arr['I' - 'A'] -= ans[6];
		arr['X' - 'A'] -= ans[6];

		ans[2] = arr['W' - 'A'];
		arr['T' - 'A'] -= ans[2];
		arr['W' - 'A'] -= ans[2];
		arr['O' - 'A'] -= ans[2];

		ans[7] = arr['S' - 'A'];
		arr['S' - 'A'] -= ans[7];
		arr['E' - 'A'] -= ans[7];
		arr['V' - 'A'] -= ans[7];
		arr['E' - 'A'] -= ans[7];
		arr['N' - 'A'] -= ans[7];

		ans[5] = arr['V' - 'A'];
		arr['F' - 'A'] -= ans[5];
		arr['I' - 'A'] -= ans[5];
		arr['V' - 'A'] -= ans[5];
		arr['E' - 'A'] -= ans[5];

		ans[4] = arr['F' - 'A'];
		arr['F' - 'A'] -= ans[4];
		arr['O' - 'A'] -= ans[4];
		arr['U' - 'A'] -= ans[4];
		arr['R' - 'A'] -= ans[4];

		ans[1] = arr['O' - 'A'];
		arr['O' - 'A'] -= ans[1];
		arr['N' - 'A'] -= ans[1];
		arr['E' - 'A'] -= ans[1];

		ans[3] = arr['T' - 'A'];

		ans[9] = arr['I' - 'A'];

		printf("Case #%d: ", z);
		for (int i = 0; i < 10; i++)
			for (int j = 0; j < ans[i]; j++)
				cout << i;
		cout << endl;
	}
	return 0;
}
