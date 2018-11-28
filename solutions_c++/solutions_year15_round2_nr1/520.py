#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <cmath>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
#include <iomanip>
#include <unordered_map>

using namespace std;

#define X first
#define Y second

using namespace std;

const int MAXN = 4000002, INF = (1<<30);
const long long RINF = 1E18;
int flip[MAXN];
int dist[MAXN];
int from[MAXN];
long long p10[30];
unordered_map<long long, long long>mp;

long long flipX(long long x) {
    long long res = 0;
    while (x > 0) {
        res = res*10 + x % 10;
        x /= 10;
    }
    return res;
}

void preprocess() {
    for (int i = 0; i < MAXN; i++) {
        int res = 0;
        int x = i;
        while (x > 0) {
            res = res*10 + x % 10;
            x /= 10;
        }
        flip[i] = res;
    }

    for (int i = 0; i < MAXN; i++) {
        dist[i] = INF;
    }
    dist[1] = 1;
    vector<int>q;
    int st = 0;
    q.push_back(1);
    while (st < q.size() ) {
        int x = q[st]; st++;
        if (x + 1 < MAXN) {
            if (dist[x + 1] > dist[x] + 1) {
                dist[x + 1] = dist[x] + 1;
                from[x + 1] = x;
                q.push_back(x + 1);
            }
        }
        if (flip[x] < MAXN) {
            if (dist[ flip[x] ] > dist[x] + 1) {
                dist[ flip[x] ] = dist[x] + 1;
                from[ flip[x] ] = x;
                q.push_back(flip[x]);
            }
        }
    }

    for (int i = 1; i < 10; i++) {
        mp[i] = i;
    }
    p10[0] = 1;
    for (int i = 1; i < 30; i++) {
        p10[i] = p10[i - 1] * 10;
    }
}

void showPath(int x) {
    while (x > 1) {
        cerr<<x<<endl;
        x = from[x];
    }
}

long long solve2(long long x) {
    if (mp.find(x) != mp.end() ) {
        return mp[x];
    }
    int len = 0;
    long long y = x;
    int dig[30];
    while (y > 0) {
        len++;
        y /= 10;
    }
    y = x;
    for (int i = len; i > 0; i--) {
        dig[i] = y % 10;
        y /= 10;
    }
    long long up = p10[len - 1], add = 0;
    if (dig[len] == 0) {
        mp[x] = solve2(x - 1) + 1;
        return mp[x];
    }
    long long A = solve2(up - 1) + 1, B = x - up;
    //cerr<<A<<" "<<up<<" "<<B<<endl;

    for (int i = 1; i < len; i++) {
        add = 0;
        for (int j = i; j > 0; j--) {
            add = add * 10 + dig[j];
        }
        long long to = up + add;
        //cerr<<to<<endl;
        if (flipX(to) <= x && flipX(to) > to) {
            B = min(B, to - up + 1 + x - flipX(to) );
        }

    }
    mp[x] = A + B;
    return A + B;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    preprocess();
    int test;
    cin>>test;
    for (int i = 1; i <= test; i++) {
        //int x;
        long long x;
        cin>>x;
        cerr<<x<<endl;
        //x = (long long)rand()*((long long)1<<30) + rand() + (long long)rand()*((long long)1<<15);
        //printf("Case #%d: %d\n", i, dist[x]);
        cout<<"Case #"<<i<<": "<<solve2(x)<<endl;
        //cerr<<solve2(x)<<endl;
        /*if (solve2(x) != dist[x]) {
            cerr<<"WA: "<<x <<" "<<solve2(x)<<" "<<dist[x]<<endl;
        }*/
        //showPath(x);
    }
    return 0;
}

