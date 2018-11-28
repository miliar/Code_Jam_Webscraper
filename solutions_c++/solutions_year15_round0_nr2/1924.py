#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define sz(a) (int)a.size()
#define fs first
#define sc second

typedef long long ll;
typedef pair<int,int> ii;

int a[1005];

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    int t, tmp;
    scanf("%d",&t);
    tmp = t;
    while (t--) {
        int n;
        scanf("%d",&n);
        for (int i = 1; i <= n; ++i)
            scanf("%d",&a[i]);
        ll res = 1000000000000000LL;
        for (int i = 1; i <= 1000; ++i) {
            ll tmp = 0;
            for (int j = 1; j <= n; ++j) {
                if (a[j] <= i) continue;
                tmp += a[j]/i + (a[j]%i!=0)-1;
            }
            res = min(res,i+tmp);
        }
        cout << "Case #" << tmp-t << ": " << res << "\n";
    }
	return 0;
}
