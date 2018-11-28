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


bool f[10];
ll func(ll n)
{
	memset(f, false, sizeof(f));
	ll i;
	int sc = 10;
	for (i = 1;sc; i++)
	{
		ll j = i*n;
		while (j)
		{
			if (!f[j % 10])
			{
				f[j % 10] = true;
				sc--;
			}
			j /= 10;
		}
	}
	return (i-1)*n;
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
	int i;
	for (i = 1; i <= turn; i++)
	{
		ll n;
		scanf("%I64d", &n);
		printf("Case #%d: ", i);
		if (n == 0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		printf("%I64d\n", func(n));
	}
	return 0;
}