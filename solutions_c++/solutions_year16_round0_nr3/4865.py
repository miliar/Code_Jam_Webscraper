//AnotherHackyCodeBySmartCoder
//GCJ_C_S.cpp
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
#define present(c,x)  ( (c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)!= (c).end() )
#define minei(x)  min_element(x.begin(),x.end())-(x).begin()
#define maxei(x)  max_element(x.begin(),x.end())-(x).begin()

#define uns(v)     sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acusum(x)  accumulate(x.begin(),x.end(),0)
#define acumul(x)  accumulate(x.begin(),x.end(),1, multiplies<int>());
#define bits(x)     __builtin_popcount( x )
#define oo INT_MAX
#define inf 1000000000

const double pi = acos(-1.0);
const double eps = 1e-11;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
void fastIO() {
	std::ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
}
map<string, vector<int> > cach;
int main() {
	fastIO();
	freopen("GCJ_C_S_O.txt","w",stdout);
	freopen("C-small-attempt0.in","r",stdin);
	int t, n, j;
	int kk = 0;
	cin >> t;
	cout << "Case #1:" << endl;
	cin >> n >> j;
	for (int i = 0; i < (1 << (n - 2)); i++) {
		string cur = "1";
		for (int k = 0; k < n - 2; k++) {
			if (((1 << k) & i) != 0) {
				cur += '1';
			} else {
				cur += '0';
			}
		}
		cur += "1";

		for (int base = 2; base <= 10; base++) {
			ll num = 0;
			for (int k = n - 1; k >= 0; k--) {
				if (cur[k] == '1')
					num += powl(base, n - k - 1);
			}
			ll div = -1;
			for (ll c = 2; c * c <= num; c++) {
				if (num % c == 0) {
					div = c;
					break;
				}
			}
			if (div != -1)
				cach[cur].pb(div);
			else
				break;
		}
		if (cach.count(cur) && sz(cach[cur]) == 9) {
			kk++;
		}
		if (kk == j)
			break;
	}
	tr(cach,it)
	{
		if (sz(it->second) != 9)
			continue;
		if (j <= 0)
			break;
		j--;
		cout << it->first << " ";
		vector<int> v = it->second;
		for (int i = 0; i < sz(v); i++) {
			cout << v[i];
			if (i != sz(v) - 1)
				cout << " ";
		}
		cout << endl;

	}
	return 0;
}
