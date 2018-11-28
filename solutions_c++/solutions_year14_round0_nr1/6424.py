#include <bits/stdc++.h>

using namespace std;

#define sz(a) (int)(a.size())

int tc,r1,x,dd,here;
map<int,int> f;

int main(){
    freopen("a.inp","r",stdin);
    freopen("magic.out","w",stdout);
    cin>>tc;
    for(int tt=1;tt<=tc;++tt){
        f.clear();dd=0;
        cin>>r1;
        for(int i=1;i<=4;++i) for(int j=1;j<=4;++j){
            cin>>x;
            if (i==r1) f[x]++;
        }
        cin>>r1;
        for(int i=1;i<=4;++i) for(int j=1;j<=4;++j){
            cin>>x;
            if (i==r1) f[x]++;
        }
        for(int i=1;i<=16;++i) if (f[i]==2) dd++,here=i;
        cout<<"Case #"<<tt<<": ";
        if (dd==0) cout<<"Volunteer cheated!\n";
        if (dd==1) cout<<here<<'\n';
        if (dd>1) cout<<"Bad magician!\n";
    }
    return 0;
}
