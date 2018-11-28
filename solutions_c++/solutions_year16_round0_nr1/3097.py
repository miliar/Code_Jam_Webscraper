#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <map>
#include <climits>
#include <set>
#include<list>
#include<string>
#include<string.h>
#include<functional>
#include<random>
#include<ctime>
typedef long long ll;
#define fast std::ios::sync_with_stdio(false);std::cin.tie(false)
#define endl "\n"
//#define abs(a) a >= 0 ? a : -a
#define ll long long
#define mod (1000000000+7)
#define Endl endl
using namespace std;
ll powmod(ll a, int b) { ll res = 1; if (a >= mod)a %= mod; for (; b; b >>= 1){ if (b & 1)res = res*a; if (res >= mod)res %= mod; a = a*a; if (a >= mod)a %= mod; }return res; }
ll gcd(ll a, ll b){ if (a < b)std::swap(a, b); return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b){ return ((a*b) / gcd(a, b)); }
int l_bound(int *arr, int lo, int hi, int val){ while (lo <= hi){ int mid = (lo + hi) >> 1; if (arr[mid] >= val)hi = mid - 1; else lo = mid + 1; }return lo; }
int u_bound(int *arr, int lo, int hi, int val){ while (lo <= hi){ int mid = (lo + hi) >> 1; if (arr[mid] > val)hi = mid - 1; else lo = mid + 1; }return hi; }
int bsearch(int *arr, int n, int val){ int lo = 0, hi = n - 1; while (hi >= lo){ int mid = (hi + lo) >> 1; if (arr[mid] == val)return mid; if (arr[mid] > val)hi = mid - 1; else lo = mid + 1; }return -1; }
const int N = 1000 + 10;
int m, ans = 0,t,cnt=0,tt=0;
ll n;
void f(ll n,int *arr){
	while (n){
		if (arr[n % 10] == 0){
			arr[n % 10] = 1;
			cnt++;
		}
		n = n / 10;
	}
	return;
}
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> t;
	while (t--){
		tt++;
		int arr[10];
		memset(arr, 0, sizeof arr);
		cnt = 0;
		scanf("%lld", &n);
		if (n == 0){
			printf("Case #%d: INSOMNIA\n", tt);
			continue;
		}
		ll num = n;
		while (1){
			f(n, arr);
			if (cnt == 10)break;
			n += num;
		}
		printf("Case #%d: %lld\n", tt, n);
	}
	return 0;
}