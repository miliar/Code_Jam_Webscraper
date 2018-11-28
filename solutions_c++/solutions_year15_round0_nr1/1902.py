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
const int N = 317;
int n = 18;
int m, x, y;
int was[36];
int d[36];
map<int64, int> id;
vector <int64> xu;
int solve()
{
	int n;
	string st;
	cin >> n;
	cin >> st;
	int ans = 0;
	int ko = 0;
	for(int i = 0; i < st.size(); ++i)
	{
		if (ko < i)
		{
			ans += i - ko;
			ko = i;
		}
		ko += st[i] - '0';
	}
	return ans;
}

int main() 
{
#ifdef WIN32
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		printf("Case #%d: %d\n", i + 1, solve());
	}
}