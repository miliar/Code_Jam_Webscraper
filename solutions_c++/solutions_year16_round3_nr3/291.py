#include<bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin>>t;
    for(int z=1; z<=t; z++) {
        int jj,pp,kk,ss;
        cin>>jj>>pp>>ss>>kk;
        cout<<"Case #"<<z<<": ";
        map<pair<int,int>,int>jp,ps,js;
        vector<pair<pair<int,int>,int> >v;
        for(int i=0; i<jj; i++) {
            for(int j=0; j<pp; j++) {
                for(int k=0; k<ss; k++) {
                    if(jp[ {i,j}]<kk && ps[ {j,k}]<kk && js[ {i,k}]<kk) {
                        jp[ {i,j}]++;
                        ps[ {j,k}]++;
                        js[ {i,k}]++;
                        v.push_back({{i+1,j+1},k+1});
                    }
                }
            }
        }
        cout<<v.size()<<"\n";
        for(int i=0; i<(int)v.size(); i++) {
            cout<<v[i].first.first<<" "<<v[i].first.second<<" "<<v[i].second<<"\n";
        }
    }
    return 0;
}
