#pragma comment(linker, "/STACK:16777216")
#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <memory.h>
#include <string.h>
#include <deque>
#include <assert.h>
#include <stack>
using namespace std;

#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define inf 2000000000
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

int t;
double c, f, x;

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cout << fixed << setprecision(7);
	cin >> t;
	FOR(tt, 1, t){
		cin >> c >> f >> x;

		double v = 2.0;
		double T = 0;
		double sum = 0;
		double ans = x/v;
		int k = 0;
		while(k < 100010){
			sum += c/v;
			v += f;
			T = sum + x/v;
			ans = min(ans, T);
			k++;
		}

		cout << "Case #" << tt << ": " << ans << endl;

	}
	
	
	
	
    return 0;
}