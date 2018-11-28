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

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
    scanf("%d\n",&t);
    int tmp = t;
    while (t--) {
        int n;
        scanf("%d ",&n);
        int res = 0, sum = 0;
        for (int i = 0; i <= n; ++i) {
            char c; scanf("%c",&c);
            int x = c-'0';
            if (sum < i) {
                res += i-sum;
                sum = i;
            }
            sum += x;
        }
        printf("Case #%d: %d\n",tmp-t,res);
    }
	return 0;
}
