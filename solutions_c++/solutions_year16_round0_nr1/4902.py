#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define sz(a) (int)a.size()
#define fs first
#define sc second

typedef long long ll;
typedef pair<int,int> ii;

vector <int> getDigit(ll k) {
    vector <int> res;
    for (; k; k /= 10)
        res.pb(k%10);
    return res;
}

void solve(ll n) {
    if (n==0) {
        printf("INSOMNIA\n");
        return;
    }
    int bit = 0; ll x = 0;
    do {
        ll k = n*(++x);
        vector <int> a = getDigit(k);
        for (int i = 0; i < sz(a); ++i)
            bit |= 1<<a[i];
    } while (bit!=1023);
    printf("%I64d\n",n*x);
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int t, tmp; scanf("%d",&t);
    tmp = t;
    while (t--) {
        int n;
        scanf("%d",&n);
        printf("Case #%d: ",tmp-t);
        solve(n);
    }
	return 0;
}
