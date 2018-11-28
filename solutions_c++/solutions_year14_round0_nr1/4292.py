#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,t=0;cin>>T;
    while (T--) {
        t++;cout<<"Case #"<<t<<": ";
        int r;cin>>r;
        int x[4];for (int i=0;i<r;i++) cin>>x[0]>>x[1]>>x[2]>>x[3];
        int f[17]={};
        for (int i=0;i<4;i++) f[x[i]]=1;
        for (int i=r;i<4;i++) cin>>x[0]>>x[1]>>x[2]>>x[3];
        cin>>r;
        for (int i=0;i<r;i++) cin>>x[0]>>x[1]>>x[2]>>x[3];
        for (int i=0;i<4;i++) f[x[i]]++;
        for (int i=r;i<4;i++) cin>>x[0]>>x[1]>>x[2]>>x[3];
        vector<int> v;
        for (int i=1;i<17;i++) if (f[i]==2) v.push_back(i);
        if (v.size()==1) cout<<v[0]<<endl;
        else if (v.size()>1) cout<<"Bad magician!\n";
        else cout<<"Volunteer cheated!\n";
    }
    return 0;        
}
