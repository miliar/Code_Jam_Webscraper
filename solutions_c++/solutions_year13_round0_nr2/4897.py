#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    int _nT; scanf("%d", &_nT);
    for(int _T=0; _T<_nT; _T++) {
        int n,m; scanf("%d%d",&n,&m);

        int h[200][200];
        for(int i=0; i<n; i++)
        for(int j=0; j<m; j++) {
            scanf("%d", &h[i][j]);
        }

        int r[200], c[200];
        for(int i=0; i<n; i++) {
            int hr=-1;
            for(int j=0; j<m; j++)
                hr = std::max(hr, h[i][j]);
            r[i] = hr;
        }
        for(int j=0; j<m; j++) {
            int hr=-1;
            for(int i=0; i<n; i++)
                hr = std::max(hr, h[i][j]);
            c[j] = hr;
        }

        bool is_ok = true;
        for(int i=0; i<n; i++)
        for(int j=0; j<m; j++) {
            int hm = std::min(r[i], c[j]);
            if(hm != h[i][j])
                is_ok = false;
        }
        printf("Case #%d: %s\n", _T+1, is_ok?"YES":"NO");
    }
    return 0;
}

