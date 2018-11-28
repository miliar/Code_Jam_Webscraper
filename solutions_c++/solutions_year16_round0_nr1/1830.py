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
int n, m;

int main()
{
	c_false;
	cin >> n;
	int C = 0;
	while(n--) {
		C++;
		cin >> m;
		if(m == 0) {
			cout << "Case #" << C << ": INSOMNIA" << endl;
			continue;
		}

		VB b(10, 0);
		int cnt = 0, k = 0;
		while(1) {
			k += m;
			int k1 = k;
			while(k1) {
				int k2 = k1 % 10;
				if(!b[k2]) cnt++, b[k2] = 1;
				k1 /= 10;
			}
			if(cnt == 10) {
				cout << "Case #" << C << ": " << k << endl; break;
			}
		}
	}

	return 0;
}


