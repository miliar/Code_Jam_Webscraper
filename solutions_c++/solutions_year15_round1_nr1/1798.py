#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE 
#include <iostream> 
#include <cstdio> 
#include <cstdlib> 
#include <vector> 
#include <sstream> 
#include <string> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <cmath> 
#include <cstring> 
#include <queue>
using namespace std; 
#pragma comment(linker, "/STACK:256000000") 
#define mp make_pair 
#define pb push_back 
#define all(C) (C).begin(), (C).end() 
#define sz(C) (int)(C).size() 
#define PRIME 1103 
#define PRIME1 31415 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef pair<int, int> pii; 
typedef vector<int> vi; 
typedef vector<vector<int> > vvi; 
//------------------------------------------------------------ 
const int N = 1000;
vi del;
int64 ans = 0;
int mas[N];
void solve()
{
	int n;
	int ans = 0, ans1 = 0;
	int rs = 0;
	scanf("%d", &n);
	
	for(int i = 0; i < n; ++i)
		scanf("%d", &mas[i]);
	for(int i = 0; i < n - 1; ++i)
	{
		ans += max(0, mas[i] - mas[i + 1]);
		rs = max(rs, mas[i] - mas[i + 1]);
	}
	for(int i = 0; i < n - 1; ++i)
	{
		ans1 += min(rs, mas[i]);
	}
	printf("%d %d\n", ans, ans1); 
}

int main() 
{
#ifdef WIN32
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int64 n;
    int x1, y1, x2, y2;
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
}