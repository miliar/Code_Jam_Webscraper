#include <bits/stdc++.h>

using namespace std;

int cnt;
bool was[10];

void add(int a){
    if (!was[a]) cnt++;
    was[a] = true;
}

void update(long long a){
    while (a != 0LL){
        add(a % 10LL);
        a /= 10LL;
    }
}

int solve(long long n){
    for (int i = 0; i < 10; ++i) was[i] = 0; cnt = 0;
    long long c = 0LL;
    for (int i = 1; ; ++i){
        c += n;
        update(c);
        if (cnt == 10) {return c;}
        if (i >= 100000) return -1;
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n; cin >> n;
    for (int i = 0; i < n; ++i){
        long long x; cin >> x;
        cout << "Case #" << i + 1 << ": ";
        int res = solve(x);
        if (res == -1) cout << "INSOMNIA" << endl;
        else cout << res << endl;
    }
    return 0;
}
