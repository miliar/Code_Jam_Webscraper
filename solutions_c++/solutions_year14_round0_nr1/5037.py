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
#include <iomanip> 
#include <functional> 
#include <bitset> 
#include <cassert> 
#include <cmath> 
#include <ctime> 
#include <queue> 
#include <list> 
#include <memory.h> 
#include <complex> 
#include <numeric> 
using namespace std; 
#pragma comment(linker, "/STACK:256000000") 
#define mp make_pair 
#define pb push_back 
#define all(C) (C).begin(), (C).end() 
#define sz(C) (int)(C).size() 
#define PRIME 1103 
#define INF ((1ll << 60) - 1) 
#define MOD 1000000007 
#define FAIL ++*(int*)0 
#define EPS 1e-11 
template<class T> T sqr(T a) {return a * a;} 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef pair<int, int> pii; 
typedef pair<int, pii> piii; 
typedef vector<int> vi; 
typedef vector<int64> vi64; 
typedef vector<pii> vpii; 
typedef vector<vector<int> > vvi; 
typedef vector<vvi> vvvi; 
typedef vector<vector<pair<int, int > > > vvpii; 
typedef vector<vector<vector<pair<int, int > > > > vvvpii; 
typedef complex<long double> cd; 
#define TASK "hobbit" 
//---------------------------------------------------------- 


void f(vi &t)
{
	int r;
	scanf("%d", &r);
	--r;
	int a[4][4];
	for(int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
		{
			scanf("%d", &a[i][j]);
			if(i == r)
				t.pb(a[i][j]);
		}
	}	
}

void solve() 
{
	vi t1, t2;
	f(t1);
	f(t2); 
	vi r;
	for(int i = 0; i < sz(t1); ++i)
	{
		for(int j = 0; j < sz(t2); ++j)
		{
			if(t1[i] == t2[j])
				r.pb(t1[i]);
		}
	}

	if(sz(r) == 0)
		puts("Volunteer cheated!");
	else if(sz(r) == 1)
		cout << r[0] << endl;
	else
		puts("Bad magician!");
}

int main() 
{ 
#ifndef ONLINE_JUDGE 
    freopen ("input.txt", "r", stdin); freopen ("output.txt", "w", stdout); 
#endif 
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; ++i)
    {
    	printf("Case #%d: ", i + 1);
    	solve(); 
    }
    return 0; 
}