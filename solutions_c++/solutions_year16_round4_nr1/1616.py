#include <bits/stdc++.h>
using namespace std;

const int N = 15;
int t, T, n, r, p, s, mr[N][3], mp[N][3], ms[N][3], k;

int main() {
    mr[0][0] = mp[0][1] = ms[0][2] = 1;
    for(int i=1; i<N; ++i) {
        for(int j=0; j<3; ++j) {
            mr[i][j] += mr[i-1][j] + mp[i-1][j];
            mp[i][j] += ms[i-1][j] + mp[i-1][j];
            ms[i][j] += ms[i-1][j] + mr[i-1][j];
        }
    }

    scanf("%d", &T);
    while(t++ < T) {
        scanf("%d%d%d%d", &n, &r, &p, &s);
        k = -1;
        for(int i=0; i<3; ++i) if (r == mr[n][i] and p == mp[n][i] and s == ms[n][i]) k = i;
        printf("Case #%d: ", t);
        if (k < 0) printf("IMPOSSIBLE\n");
        else {
            string u, v;
            u += !k ? "R" : k == 1 ? "P" : "S";
            for(int i=0; i<n; ++i) {
                v.clear();
                for(int j=0; j<u.size(); ++j) {
                    if (u[j] == 'P') v += "PR";
                    else if (u[j] == 'R') v += (i == n-1) ? "RS" : "SR";
                    else v += (i < n-2) ? "SP" : "PS";
                }
                swap(u, v);
            }
            printf("%s\n", u.c_str());
        }
    }
    return 0;
}
