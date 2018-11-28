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
const int N = 100000 + 10;
int m, ans = 0,t,cnt=0,tt=0,prv,n,mx;
bool prime[N+1];
int sp[N + 1];
ll ppow[12][20];

void build(){
	for (int i = 1; i < 11; i++){
		ppow[i][0] = 1;
		for (int j = 1; j < 17; j++){
			ppow[i][j] = ppow[i][j - 1] * i;
		}
	}
}

ll is_prime(ll n){
	if (n == 2 || n == 3 || n == 5 || n == 7)
		return 0;
	for (ll i = 2; i <= sqrt(n) + 1; i++){
		if (n % i == 0)
			return i;
	}
	return 0;
}

bool check(int *arr, int n,vector<ll> &v){
	for (int i = 2; i <= 10; i++){
		ll num = 0;
		for (int j = 0; j < n; j++){
			num += arr[j] * ppow[i][j];
		}
		ll k = is_prime(num);
		if (k == 0 || k == num)
			return 0;
		v.push_back(k);
	}
	return 1;
}

int main(){
	freopen("input.in", "r", stdin);
	freopen("C.out", "w", stdout);
	build();
	scanf("%d %d %d", &t, &n, &mx);
	printf("Case #1:\n");
	ll all = (1 << (n - 2));
	int *arr = new int[n + 1];
	arr[0] = 1;
	arr[15] = 1;
	for (ll i = 0; i <= all; i++){
		for (int i = 1; i < n - 1; i++)arr[i] = 0;
		ll who = i,k = 1;
		//cout << who << endl;
		while (who){
			arr[k++] = who % 2;
			who = who/2;
		}
		//for (int i = 0; i < n; i++)cout << arr[i] << " "; cout << endl;
		vector<ll> v;
		if (check(arr, n, v)){
			cnt++;
			for (int i = n-1; i >= 0; i--)
				printf("%d", arr[i]);
			printf(" ");
			for (int i = 0; i < v.size(); i++)
				printf("%lld ", v[i]);
			printf("\n");
		}
		if (cnt == mx)
			break;
	}
	return 0;
}