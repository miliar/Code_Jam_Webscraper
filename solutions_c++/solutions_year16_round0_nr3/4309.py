#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair <int, int> pii;
#define x first
#define y second
#define mp make_pair
#define pb push_back
const int N = (int)1e5 + 5, INF = (int)1e9;
const ld EPS = 1e-9;

vector <int> v;
int n, j, d[15];

void gen(int i){
	if(i == n - 1){
		v.pb(1);
		for(int c = 2; c < 11; c++){
			ll s = 0, c1 = 1;
			for(int k = n - 1; k >= 0; k--, c1 *= c)
				s += v[k] * c1;
			int x = (int)sqrt(s) + 5;
			d[c] = 0;
			for(int y = 2; y <= x; y++)
				if(s % y == 0){
					d[c] = y;
					break;
				}
			if(d[c] == 0){
				v.pop_back();
				return;
			}
		}
		for(int k = 0; k < n; k++)
			cout << v[k]; cout << " ";
		for(int c = 2; c < 11; c++)
			cout << d[c] << " "; cout << "\n";
		j--;
		if(j == 0)
			exit(0);
		v.pop_back();
		return;
	}
	v.pb(0);
	gen(i + 1);
	v.pop_back(); v.pb(1);
	gen(i + 1);
	v.pop_back();
}

int main()
{
	freopen("b.txt", "r", stdin);
	freopen("a.txt", "w", stdout);
	cin >> n >> n >> j;
	cout << "Case #1:\n";
	v.pb(1);
	gen(1);
	return 0;
}