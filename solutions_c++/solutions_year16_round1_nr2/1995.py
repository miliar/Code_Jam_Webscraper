#include <bits/stdc++.h>
using namespace std;

const int N = 51;
int t, T, n, n0, l[2*N][N], id[2*N], k, r[N], ok;
map<int, int> st;

bool cp(int i, int j) {return l[i][k] > l[j][k];}

int main() {
    scanf("%d", &T);
    while(t++ < T) {
        scanf("%d", &n0);
        ok = 1;
        n = n0;
        for(int i=0; i<2*n-1; ++i) for(int j=0; j<n; ++j) scanf("%d", &l[i][j]);

        for(int i=0; i<2*n-1; ++i) id[i] = i;

        for(k=0; k<n0-1; ++k) {
            st.clear();
            sort(id, id+2*n-1, cp);

            if (l[id[2*n-2]][k] != l[id[2*n-3]][k]) {
                for(int i=0; i<2*n-1; ++i) st[l[id[i]][k]]++;
                for(int i=k+1; i<n0; ++i) st[l[id[2*n-2]][i]]--;
                for(auto i = st.begin(); i != st.end(); ++i) while((i->second)--) r[k++] = i->first;
                ok = 0;

                break;
            }

            for(int i=k+1; i<n0; ++i) st[l[id[2*n-2]][i]]++, st[l[id[2*n-3]][i]]++;
            n--;
            for(int i=0; i<2*n-1; ++i)
                (st[l[id[i]][k]] > 1) ? st[l[id[i]][k]]-- : st.erase(l[id[i]][k]);
            r[k] = st.begin()->first;
        }

        while(!st.begin()->second) st.erase(st.begin());
        if (ok) r[k] = l[id[0]][k];

        printf("Case #%d: ", t);
        for(int i=0; i<n0; ++i) printf("%d ", r[i]);
        printf("\n");
    }
    return 0;
}
