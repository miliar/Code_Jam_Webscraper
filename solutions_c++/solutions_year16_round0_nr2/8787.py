#pragma comment(linker,"/STACK:64000000")
#include <stdio.h>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <iterator>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
#define mp make_pair
#define pb push_back
#define eps (double)(1e-2)
#define MOD (ll)(1e9 + 7)

const int maxlen = 1e5 + 10;
const int length_double = 100;
const int base = 10;
#define PI 3.14159265358979323846
#define name "game"

string s;

void rev_i(int k)
{
	for (int i = 0; i <= k; ++i)
		s[i] = '+' + '-' - s[i];
	return;
}
int solve()
{
	int i=0;
	int ans = 0;
	while (i != -1)
	{
		i = s.size() - 1;
		while (i >= 0 && s[i] == '+')
			i--;
		if (i == -1)
			break;
		rev_i(i);
		ans++;
	}
	return ans;
}
int main()
{
#ifdef _DEBUG
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	/*#else
	freopen(name".in", "rt", stdin);
	freopen(name".out", "wt", stdout);*/
#endif
	int turn;
	scanf("%d", &turn);
	for (int i = 1; i <= turn; ++i)
	{
		printf("Case #%d: ",i);
		cin >> s;
		printf("%d\n", solve());
	}
	return 0;
}