//~In The Name Of Allah~//
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <cmath>
#include <string.h>
#include <sstream>
#include <cstring>
#include <fstream>
#include <functional>
#include <cstdio>
#include <stack>
#include <utility> 
#include <set>
#include <list>
#include <queue>
#include <bitset>
using namespace std;

#define all(S) S.begin(), S.end()
#define rall(S) S.rbegin(), S.rend()
#define mem(C, V) memset(C, V, sizeof C)
#define sp(N) setprecision(N)<<fixed
#define siz(S) (int)S.size()
#define rz(S, N) S.resize(N)
#define rep(i, j) for (int i = 0; i < int(j); i++)
#define Rep(i, j, k) for (int i = (int)j; i < (int)k; i++)
#define srep(S) for (auto it:S)
#define Theta(A) acos((double)A)*180.0 / Pi
#define getdis(xa, ya, xb, yb) double(sqrt((xa - xb)*(xa - xb) + (ya - yb)*(ya - yb)))
#define slope(xa, ya, xb, yb) ((double)yb-(double)ya)/((double)xb-(double)xa)

#define Read() freopen("input.txt", "r", stdin)
#define Write() freopen("output.txt", "w", stdout)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<ll> vll;
typedef vector<string> vs;

const double Pi = 2.0 * acos(0.0);

const double Ex = 2.7182818284;
const int Mod = 1000000007;
const int oo = 2e9 + 1;

int di[] = { 0, 1, 0, -1 };
int dj[] = { 1, 0, -1, 0 };
int dik[] = { 1, 1, 2, 2, -1, -1, -2, -2 };
int djk[] = { 2, -2, 1, -1, -2, 2, -1, 1 };

ll gcd(ll x, ll y){ return !y ? x : gcd(y, x%y); }

int main(){
	Read(), Write();
	int test, n, ans, tmp, idx;
	char str[1005];
	scanf("%d", &test), idx = 0;
	while (test-- && scanf("%d%s", &n, &str)){
		ans = 0, tmp = str[0] - '0';
		Rep(i, 1, n + 1) if (i > tmp && str[i] - '0')
			ans += (i - tmp), tmp += (i - tmp) + (str[i] - '0');
		else tmp += (str[i] - '0');
		printf("Case #%d: %d\n", ++idx, ans);
	}
	return 0;
}