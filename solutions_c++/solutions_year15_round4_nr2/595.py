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
#define y1 asdf
#define y2 asdqwer
const int N = 110;
double EPS = 1e-10;
double t[2], r[2];
int n;
double x, v;
void solve()
{
	/*int n, int x, int v;
	int tx, int tv;
	scanf("%d %d.%d %d.%d", &n, &v, &tv, &x, &tx); 
	x = x * 10000 + tx;
	v = v * 10000 + tv;
	for(int i = 0; i < n; ++i)
	{
		int t1, t2, t3, t4;
		scanf("%d.%d %d.%d", &t1, &t2, &t3, &t4);
		t1 = t1 * 10000 + t2;
		t3 = t3 * 10000 + t4;
		r = t1;
		t = 
	}*/
	cin >> n >> v >> x;
	//cerr << n << ' ' << v << ' ' << x << endl;
	for(int i = 0; i < n; ++i)
		cin >> r[i] >> t[i];
	cout.precision(8);
	cout << fixed;
	if (n == 2 && abs(t[0] - t[1]) < EPS)
	{
		r[0] += r[1];
		n = 1;
	}
	if (n == 1)
	{
		if(abs(t[0] - x) > EPS)
		{
			cout << "IMPOSSIBLE";
			return;
		}
		//cerr << v << ' ' << r[0] << endl;
		cout << v / r[0];
		return;
	}
	double ans = 1e10;
	double v0 = v * (x - t[1]) / (t[0] - t[1]);
	double v1 = v - v0;
	//cerr << v0 << ' ' << v1 << endl;
	if (v0 < -EPS || v1 < -EPS)
		cout << "IMPOSSIBLE";
	else
	{
		double p = v0 / r[0], p1 = v1 / r[1];
		if (abs(p - p1) < EPS)
		{
			cout << p; 
			return;
		}
		if (p > p1)
			cout << p;
		else
			cout << p1;
	}
	

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
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}