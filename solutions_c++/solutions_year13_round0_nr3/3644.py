#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <math.h>
#include <queue>
#include <string.h>
#include <sstream>
#define fo(i,n) for(i=0;i<n;i++)
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back
#define mp make_pair
using namespace std;

typedef long long ll;

int add(int a, int b, int c) {
    if (c < a || c > b) return 0;
    return 1;
}

int main(void) {
    int t, tt;
    cin >> t;
    fo(tt,t) {
        int a, b;
        cin >> a >> b;
        int ans = 0;
        ans += add(a, b, 1);
        ans += add(a, b, 4);
        ans += add(a, b, 9);
        ans += add(a, b, 121);
        ans += add(a, b, 484);
        cout << "Case #" << tt + 1 << ": " << ans << endl;
    }
}
