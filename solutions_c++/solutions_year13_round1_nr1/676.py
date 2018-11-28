#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <sstream>
typedef long long ll;
using namespace std;

#define FORi(n) for(int i=0;i<n;++i)
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())

string inttostr (int a) {
    string s;
    ostringstream os;
    os << a;
    s = os.str();
    return s;
}

size_t high(ll a) {
    size_t bits=0;
    while (a!=0) {
        ++bits;
        a>>=1;
    };
    return bits;
}

ll sumcol (ll k, ll R) {
	if (high(k)+high(R) >= 64) return 2000000000000000001;
	else return k*(2*R + 1) + 2*k*(k-1);
}

ll binsearch(ll R, ll S) {
	ll min_k = 0;
	ll max_k = 1000000000;
	ll left = min_k;
	ll right = max_k;
	ll mid = (left+right)/2;
	while (right-left>1) {
		ll test = sumcol(mid,R);
		if (test > R && test < 2000000000000000001 && test <= S) {
			left = mid;
		} else {
			right = mid;
		}
		mid = (left+right)/2;
	}
	return left;
}

void solve () {
	int Ntests = 0;
	cin >> Ntests;
	for (int test_id = 1; test_id <= Ntests; test_id++) {
		ll R, S;
		cin >> R >> S;
		cout << "Case #" << test_id << ": " << binsearch(R,S) << endl;
	}
}

void main()
{
    #ifdef _DEBUG
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    solve();
}