//I_HAVE_A_DREAM
//C.Dijkstra_small.cpp
//DreamBig
//Apr 11, 2015
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
#define MAXN 10010
int Is[MAXN], Js[MAXN], Ks[MAXN], n;
int sn(int nm) {
	return nm > 0 ? 1 : -1;
}
int mat[6][6] = { { 0, 0, 0, 0, 0 }, { 0, 1, 2, 3, 4 }, { 0, 2, -1, 4, -3 }, {
		0, 3, -4, -1, 2 }, { 0, 4, 3, -2, -1 } };

int conv(int a, int b) {
	int signa = sn(a);
	int signb = sn(b);
	a = abs(a);
	b = abs(b);
	if (signa == signb) return mat[a][b];
	return -1 * mat[a][b];

}
void MEMSET() {
	memset(Is, 0, sizeof Is);
	memset(Ks, 0, sizeof Ks);
	memset(Js, 0, sizeof Js);

}
int main() {
	std::ios_base::sync_with_stdio(0);
	freopen("C-small-attempt4.out", "w", stdout);
	freopen("C-small-attempt4.in", "r", stdin);

	//a*b=c
	//a*-c=b
	int TC, X, L;
	cin >> TC;
	for (int T = 1; T <= TC; T++) {
		MEMSET();
		cin >> L >> X;
		vector<int> I, J, K;
		string s;
		cin >> s;
		string tmp = s;
		X--;
		while (X--) {
			s += tmp;
		}

		n = sz(s);
		string ans = "NO";
		Is[0] = (s[0] - 'i') + 2;
		if (Is[0] == 2) I.pb(0);
		for (int i = 1; i < n; i++) {
			Is[i] = conv(Is[i - 1], (s[i] - 'i') + 2);
			if (Is[i] == 2) I.pb(i);
		}

		for (int i = 0; i < n; i++) {
			Ks[i] = (i == 0 ? Is[n - 1] : conv((Is[i - 1]), (-1 * Is[n - 1])));
			if (Ks[i] == 4) K.pb(i);
		}
		bool flg = true;
		for (int i = 0; i < sz(I) && flg; i++) {
			for (int j = 0; j < sz(K) && flg; j++) {
				if (K[j] <= I[i] + 1) continue;

				int fp = Ks[I[i]+1];
				int rs = conv(-1 * fp, Ks[K[j]]);

				if (rs == 3) {
					ans = "YES";
					flg = false;
				}
			}
		}
		cout << "Case #" << T << ": " << ans << "\n";

	}
	return 0;
}
