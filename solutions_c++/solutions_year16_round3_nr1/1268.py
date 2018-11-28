#include <bits/stdc++.h>

using namespace std;

const int N = 1e3 + 10;

int tests;

int p[N], n, sz;
priority_queue<pair<int, int> > q;
string ans[N];

void input_data(){
    cin >> n;
    while (!q.empty()) q.pop();
    for (int i = 0; i < n; ++i) cin >> p[i];
    for (int i = 0; i < n; ++i) q.push(make_pair(p[i], i));
}

void solve(){
    int cnt = 0;
    for (int i = 0; i < n; ++i) cnt += p[i];
    sz = 0;
    while (!q.empty()){
        ans[sz] = "";
        int m1 = q.top().second;
        int p1 = q.top().first;
        q.pop();
        p1--;
        ans[sz] += char('A' + m1);
        cnt--;
        if (p1 != 0)
            q.push(make_pair(p1, m1));
        if (q.empty()) {sz++; break;}
        int m2 = q.top().second;
        int p2 = q.top().first;
        q.pop();
        if (p2 > cnt / 2){
            p2--;
            cnt--;
            if (p2 != 0)
            q.push(make_pair(p2, m2));
            ans[sz] += char('A' + m2);
        } else {
            q.push(make_pair(p2, m2));
        }
        sz++;
    }
}

void output_data(int test){
    cout << "Case #" << test << ": ";
    for (int i = 0; i < sz; ++i) cout << ans[i] << " ";
    cout << endl;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tests;
    for (int test = 1; test <= tests; ++test){
        input_data();
        solve();
        output_data(test);
    }
    return 0;
}
