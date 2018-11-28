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

#ifndef ONLINE_JUDGE
#define gc getchar
#else
#define gc getchar_unlocked
#endif // !ONLINE_JUDGE

#define all(S) S.begin(), S.end()
#define rall(S) S.rbegin(), S.rend()
#define sp(N) setprecision(N)<<fixed
#define siz(S) (int)S.size()
#define rep(i, j) for (int i = 0; i < int(j); i++)
#define Rep(i, j, k) for (int i = (int)j; i < (int)k; i++)
#define srep(S) for (auto it:S)
#define mem(U, V) memset(U, V, sizeof U)
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

int di[] = { 0, 1, 0, -1, 1, 1, -1, -1 };
int dj[] = { 1, 0, -1, 0, 1, -1, -1, 1 };
int dik[] = { -1, -1, 1, 1, -2, -2, 2, 2 };
int djk[] = { 2, -2, 2, -2, 1, -1, 1, -1 };

ll gcd(ll x, ll y){ return !y ? x : gcd(y, x%y); }

void getInt(int &ret){
	char tmpc;
	while (tmpc = getchar(), tmpc<'0' || tmpc>'9');
	ret = tmpc - '0';
	while (tmpc = getchar(), tmpc >= '0' && tmpc <= '9')
		ret = ret * 10 + tmpc - '0';
}
bool vis[(int)1e7 + 10];
int main(){
	Read(), Write();
	int test, idx = 0;
	cin >> test;
	while (test--){
		int n, best, ans = 1;
		cin >> n;

		mem(vis, 0);
		queue<pii> q;
		q.push(make_pair(1, 1));
		while (!q.empty()){
			int x, y, tmp = 0, now;
			x = q.front().first, y = q.front().second;
			now = x;
			q.pop();
			if (x == n){
				ans = y;
				break;
			}
			if (vis[x]) continue;
			now = x, vis[x] = 1;
			while (now) tmp = tmp * 10 + (now % 10), now /= 10;
			q.push(make_pair(x + 1, y + 1));
			q.push(make_pair(tmp, y + 1));
		}
		cout << "Case #" << ++idx << ": " << ans << endl;
	}
	return 0;
}