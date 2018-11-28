//I_HAVE_A_DREAM
//A.cpp
//DreamBig
//May 2, 2015
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
ll N;
#define MAXN 1000007
int dp[MAXN];
int rev(int n) {
	int re = 0;
	while (n) {
		re *= 10;
		re += (n % 10);
		n /= 10;
	}
	return re;
}

int main() {
	std::ios_base::sync_with_stdio(0);
freopen("A-small-attempt0.out","w",stdout);
freopen("A-small-attempt0.in","r",stdin);

	for (int i = 0; i <= MAXN; i++)
		dp[i] = i;
	int rv;
	for (int i = 1; i <= MAXN; i++) {
		rv = rev(i);
		if (i + 1 <= MAXN) dp[i + 1] = min(dp[i + 1], dp[i] + 1);
		if (rv <= MAXN) dp[rv] = min(dp[rv], dp[i] + 1);

	}

	int TC;
	cin >> TC;
	for (int T = 1; T <= TC; T++) {
		cin >> N;
		cout << "Case #" << T << ": " << dp[N];
		if (T != TC) cout << endl;
	}
	return 0;
}
