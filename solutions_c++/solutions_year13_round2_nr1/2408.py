#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <utility>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <sstream>
#define INF 1e9
#define pb push_back
#define mp make_pair
#define forn(i,n) for (int i = 0; i < n; i++)

using namespace std;

typedef long long ll;

int s[105], n, a;
int z[105][1000005];

int howMuch(int k, int w, int &moves) {
    if (w > k)
        return w + k;
    if (w == k) {
        moves++;
        return w + w - 1 + k;
    }
    while (w <= k) {
        if (w == k) {
            moves++;
            return w + w - 1 + k;
        } else {
            moves++;
            w += w - 1;
        }
    }
    return w + k;
}

string tostring(int i) {
    stringstream ss;
    ss << i;
    return ss.str();
}

int getAns(int k = 0, int w = a) {
    //cout << k << ' ' << w << endl;
    if (z[k][w] != INF)
        return z[k][w];
    if (k >= n)
        return z[k][w] = 0;
    if (w > s[k]) {
        return z[k][w] = getAns(k + 1, w + s[k]);
    } else {
        int steps = 0;
        int val = howMuch(s[k], w, steps);
      //  cout << "!!!" << val << endl;
        return z[k][w] = min(getAns(k + 1, val) + steps
                            , getAns(k + 1, w) + 1);
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;

    for (int q = 0; q < T; q++) {
        cin >> a >> n;
        for (int i = 0; i < n; i++)
            cin >> s[i];
        sort(s, s + n);
        for (int i = 0; i < 100; i++)
            for (int j = 0; j < 1000000; j++)
                z[i][j] = INF;
        int ans = 0;
        if (a == 1)
            ans = n;
        else
            ans = getAns();
        cout << "Case #" << tostring(q + 1) << ": " << ans << endl;
    }

    return 0;
}
