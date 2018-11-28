#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <set>
#include <memory.h>
#include <string.h>
#include <sstream>
#include <queue>
#include <bitset>

using namespace std;

//Loops
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define MEM(a,b) memset((a),(b),sizeof(a))

//Constants
#define inf 1000000000
#define pi 2*acos(0.0)
#define eps 1e-9

//Functions
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sz(x) int((x).size())

//Pairs
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

//Input-Output
#define FREOPEN(a,b) freopen(a,"r",stdin); freopen(b,"w",stdout);

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

const int mod = int(1e9) + 7;

#define N 1010

int a[N] = { 0 };

int Solve1(int n){
	int ans = 0;
	for (int i = 0; i + 1 < n; i++)
	if (a[i] > a[i + 1])ans += a[i] - a[i + 1];
	return ans;
}
int Solve2(int n){
	int ans = 0, cur = 0;
	for (int i = 0; i + 1 < n; i++)cur = max(cur, a[i] - a[i + 1]);
	for (int i = 0; i + 1 < n; i++){
		ans += min(cur, a[i]);
	}
	return ans;
}

int main()
{
	FREOPEN("input.txt", "output.txt");
	int test, n;
	scanf("%d", &test);
	for (int t = 0; t < test; t++){
		scanf("%d", &n);
		for (int i = 0; i < n; i++)scanf("%d", &a[i]);
		printf("Case #%d: %d %d\n", t + 1, Solve1(n), Solve2(n));
	}
	return 0;
}
