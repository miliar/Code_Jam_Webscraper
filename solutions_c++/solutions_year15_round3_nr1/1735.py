using namespace std;
#include <bits/stdc++.h>
#define fdto(i, r, l) for(int i = r; i >= l; --i)
#define fto(i, l, r) for(int i = l; i <= r; ++i)
#define forit(it, type, var) for(type::iterator it = var.begin(); it != var.end(); it++)
#define ii pair<int, int>
#define iii pair<int, ii>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ll long long
#define maxN 100005
#define mod 1000000009



int main () {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    int nTest;
    scanf("%d", &nTest);
    fto(iTest, 1, nTest) {
        int r, c, w;
        scanf("%d%d%d", &r, &c, &w);
        int ans = 0, i = 0;
        while (c-i > w*2-1) {
            i+=w;
            ++ans;
        }
        if (c-i > w) ans+=w+1;
        else ans+=w;
        printf("Case #%d: %d\n", iTest, ans);
    }

    return 0;
}
