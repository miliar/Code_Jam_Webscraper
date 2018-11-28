#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
#include<bitset>
using namespace std;

ofstream out("tttt");

const int N = 1010;

int n, s, x[N], y[N], z[N];
double d[N];

double dist(int a, int b) {
    return sqrt((x[a] - x[b]) * (x[a] - x[b]) + (y[a] - y[b]) * (y[a] - y[b]) + (z[a] - z[b]) * (z[a] - z[b]));
}

bool ver[N];

void calcd(int nod) {
    int i;
    memset(ver, 0, sizeof(ver));
    queue<int> q;

    q.push(nod);
    ver[nod] = 1;

    while(!q.empty()) {
        int el = q.front();
        ver[el] = 0;
        q.pop();

        for(i = 1; i <= n; ++i) if(d[i] > max(d[el], dist(el, i))) {
            d[i] = max(d[el], dist(el, i));
            if(!ver[i]) {
                ver[i] = 1;
                q.push(i);
            }
        }
    }
}

void sol() {
    int i, j, t;

    cin >> n >> s;

    for(i = 1; i <= n; ++i) {
        cin >> x[i] >> y[i] >> z[i] >> t >> t >> t;
        d[i] = 2000000000;
    }

    d[1] = 0;
    calcd(1);

    out << fixed << setprecision(12) << fixed << d[2];
}

int main() {
    freopen("ttt", "r", stdin);
    //freopen("tttt", "w", stdout);

    int t, a = 0;
    cin >> t;

    while(t--) {
        ++a;
        out << "Case #" << a << ": ";
        sol();
		out << "\n";

        printf("Test %d\n", a);
    }

    return 0;
}
