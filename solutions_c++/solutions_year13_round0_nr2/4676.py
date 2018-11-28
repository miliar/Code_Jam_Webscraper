#include <iostream>
#include <cstdio>
using namespace std;

int n,m,a[200][200];
int cas;

int main() {

    freopen("p2.in","r",stdin);
    freopen("p2.out","w",stdout);
    cin>>cas;
    int C = cas;

    while (cas-->0) {
        cin>>n>>m;
        for (int i=0;i<n;++i)
            for (int j=0;j<m;++j)
                cin>>a[i][j];

        bool res = true;
        for (int i=0;i<n;++i) {
            if (!res) break;
            for (int j=0;j<m;++j) {
                if (!res) break;
                int p = 0;
                for (int u=0;u<m;++u)
                    if (u!=j && a[i][u]>a[i][j]) {
                        p++;
                        break;
                    }

                for (int u=0;u<n;++u)
                    if (u!=i && a[u][j]>a[i][j]) {
                        p++;
                        break;
                    }

                if (p==2)
                    res = false;
            }
        }

        if (res)
            cout<<"Case #"<<C-cas<<": YES"<<endl;
        else
            cout<<"Case #"<<C-cas<<": NO"<<endl;

    }
}
