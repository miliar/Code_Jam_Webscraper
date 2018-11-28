//84104971101048411497 - Can you guess what does this mean?
using namespace std;
#include <bits/stdc++.h>
#define mapii map<int, int>
#define debug(a) cout << #a << ": " << a << endl
#define debuga1(a, l, r) fto(i, l, r) cout << a[i] << " "; cout << endl
#define fdto(i,  r, l) for(int i = (r); i >= (l); --i)
#define fto(i, l, r) for(int i = (l); i <= (r); ++i)
#define forit(it, var) for(__typeof(var.begin()) it = var.begin(); it != var.end(); it++)
#define fordit(rit, var) for(__typeof(var.rbegin()) rit = var.rbegin(); rit != var.rend(); rit++)
#define ii pair<int, int>
#define iii pair<int, ii>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define ll long long
#define maxN 105

template <class T>
T min(T a, T b, T c) {
    return min(a, min(b, c));
}

template <class T>
T max(T a, T b, T c) {
    return max(a, max(b, c));
}

int nTest, n, f1[maxN], f2[maxN];
//f1: happy
//f2: unhappy
string s;

int main () {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    scanf("%d", &nTest);
    fto(iTest, 1, nTest) {
        cin >> s;
        n = s.length();

        fto(i, 1, n) {
            if (s[i-1] == '-') {
                f1[i] = min(f1[i-1]+2, f2[i-1]+1);
                f2[i] = min(f1[i-1]+1, f2[i-1]);
            }
            else {
                f2[i] = min(f2[i-1]+2, f1[i-1]+1);
                f1[i] = min(f2[i-1]+1, f1[i-1]);
            }
        }
        printf("Case #%d: %d\n", iTest, f1[n]);
    }

    return 0;
}
