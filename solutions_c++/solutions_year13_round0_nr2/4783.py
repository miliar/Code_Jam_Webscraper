#include <iostream>
#include <string>
using namespace std;

int n,m;
int a[100][100];

int main() {
    int TT;
    cin>>TT;
    for(int T=1;T<=TT;T++) {
        cin>>n>>m;
        for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin>>a[i][j];
        cout<<"Case #"<<T<<": ";
        bool ans=true;
        while(true) {
            int m0=999, mi,mj;
            for(int i=0;i<n;i++)for(int j=0;j<m;j++) if (a[i][j]<m0) {
                m0=a[i][j];
                mi=i; mj=j;
            }
            if (m0==999) break;
            bool row=true;
            for(int j=0;j<m;j++) if ((a[mi][j]>m0)&&(a[mi][j]!=999)) {row=false; break;}
            if (row) {
                for(int j=0;j<m;j++) a[mi][j]=999;
                continue;
            }
            bool col=true;
            for(int i=0;i<n;i++) if ((a[i][mj]>m0)&&(a[i][mj]!=999)) {col=false; break;}
            if (col) {
                for(int i=0;i<n;i++) a[i][mj]=999;
                continue;
            }
            ans=false; break;
        }
        if (ans) cout<<"YES";
        else cout<<"NO";
        cout<<endl;
    }
    return 0;
}