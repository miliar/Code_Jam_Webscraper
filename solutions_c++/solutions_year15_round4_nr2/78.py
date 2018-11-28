#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

const double EPS = 1e-9;

void solve(int test)
{
    printf("Case #%d: ", test);
	int n; double V, X;
	cin >> n >> V >> X;

	double r[2], c[2];
	forn(i, n) cin >> r[i] >> c[i];

    if (n == 1)
    {
    	if (abs(X - c[0]) < EPS)
    	{
    		cout << V / r[0] << endl;		
    	}
    	else cout << "IMPOSSIBLE\n";
    	return;
    }

    // n = 2


    if (abs(c[0] - c[1]) < EPS)
    {
    	if (abs(X - c[0]) < EPS)
    	{
    		cout << V / (r[0] + r[1]) << endl;
    	}
    	else cout << "IMPOSSIBLE\n";
    	return;
    }

    double v[2];

    v[0] = V * (c[1] - X) / (c[1] - c[0]);
    v[1] = V * (X - c[0]) / (c[1] - c[0]);

    if (v[0] < -EPS || v[1] < -EPS) 
    {
    	cout << "IMPOSSIBLE\n";
    	return;
    }

    cout << max(v[0] / r[0], v[1] / r[1]) << endl;

}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    cout.precision(10);
    cout << fixed;

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}
