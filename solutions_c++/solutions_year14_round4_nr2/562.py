#include <iostream>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

int n,m;
int a[1111];

int main() {
    int TT;
    cin>>TT;
    for(int T=1;T<=TT;T++) {
        cin>>n;
        for(int i=0;i<n;i++) cin>>a[i];
        int wl=0,wr=n-1,ans=0;
        for(int p=0;p<n;p++) {
            int m=2147483647,mm=0;
            for(int i=wl;i<=wr;i++) if (a[i]<m) {
                m=a[i];
                mm=i;
            }
            int tl=mm-wl, tr=wr-mm;
            if (tl<tr) {
                ans+=tl;
                //cout<<mm<<' '<<m<<" l "<<wl<<endl;
                for(int i=mm;i>wl;i--) a[i]=a[i-1];
                a[wl]=m;
                wl++;
            } else {
                ans+=tr;
                //cout<<mm<<' '<<m<<" r "<<wr<<endl;
                for(int i=mm;i<wr;i++) a[i]=a[i+1];
                a[wr]=m;
                wr--;
            }
        }
        cout<<"Case #"<<T<<": ";
        cout<<ans;
        cout<<endl;
    }
    return 0;
}