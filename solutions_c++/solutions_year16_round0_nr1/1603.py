#include <bits/stdc++.h>
#define MAXN 100002
#define INF 1000000
using namespace std;
typedef long long ll;
typedef int char_32;
#define MAXN1 100002
#define INF2 1000000
#define MAXN3 100002
#define INF4 1000000
#define MAXN5 100002
#define INF6 1000000
#define MAXN7 100002
#define INF8 1000000
#define MAXN9 100002
#define INF10 1000000
#define MAXN11 100002
#define INF12 1000000
#define MAXN13 100002
#define INF14 1000000
#define MAXN15 100002
#define INF16 1000000

int used[10];

char_32 main() {
    //srand(time(0));
    freopen("A-large.in", "r", stdin);
    freopen("condense2.out", "w", stdout);
    int t; cin >> t;
    for(int z = 1; z <= t; ++z) {
    memset(used, 0, sizeof used);
    ll n, k = 0; cin >> n;

    if(n == 0) {
        cout << "Case #" << z << ": " << "INSOMNIA" << endl;
    }

    for(int i = 1; i < 1000; ++i) {

        ll t = 1LL * n * i;
        while(t) {
            if(!used[t % 10]) used[t % 10] = 1, k += 1;
            t /= 10;
        }
        if(k == 10) {
            cout << "Case #" << z << ": " << 1LL * n * i << endl;
            break;
        }

    }

    }


}
