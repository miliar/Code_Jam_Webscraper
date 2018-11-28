#include <stdio.h>
#include <stdlib.h>
#include<iostream>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <string.h>
#include <string>
#include <limits.h>
#include <algorithm>
#include <set>
#include <ctime>
#include <cmath>
#include <assert.h>
using namespace std;
#define SZ(x) ((int)(x).size())
#define rep(i,a,n) for (int i=a; i<(int)n; i++)
#define per(i,n,a) for (int i=n; i>=a; i--)
#define hk push_back
#define pk pop_back
#define mp make_pair
#define PI 3.141592653589793
#define clr(a) memset(a, 0, sizeof(a))
#define clr1(a) memset(a, -1, sizeof(a))
#define endl "\n"
#define c_false ios_base::sync_with_stdio(false); cin.tie(0)
typedef vector<int> VI;
typedef vector< pair<int, int> > VIP;
typedef vector< pair<int, pair<int, double> > > VIPP;
typedef vector<string> VS;
typedef vector <double> VD;
typedef vector <bool> VB;
typedef long long ll;
const ll mod = 1000000007;
ll powmod(ll a, ll b) {
 ll res = 1; a %= mod; for (; b; b >>= 1){ if (b & 1)res = res*a%mod; a = a*a%mod; }return res;
}

#define MAX_V 100005
int n, K, C, S;

int main()
{
	c_false;
	cin >> n;
	int T = 0;
	while(n--) {
		T++;
		cin >> K >> C >> S;

		cout << "Case #" << T << ": ";

		if(C == 1) {
			if(S < K) cout << "IMPOSSIBLE" << endl;
			else {
				rep(i, 1, K + 1) cout << i << " ";
				cout << endl;
			}
		}
		else {
			if(S < (K + 2) / 2) cout << "IMPOSSIBLE" << endl;
			else {
				int p = (K + 1) / 2;
				rep(i, 0, p) {
					ll K2 =  K * i + (K - i);
					cout << K2 << " ";
				}
				cout << endl;
			}
		}
	}

	return 0;
}


