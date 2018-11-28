#include <bits/stdc++.h>
using namespace std;

int main(){
    std::ios::sync_with_stdio(false);
    freopen("B-large.in","r",stdin);
    freopen("lolzano.out","w",stdout);
    int t; cin >> t;
    for( int i = 1 ; i <= t ; ++i ){
        int n, x; cin >> n;
        int aux = (2*n*n)-n;
        map<int,int>mp;
        for( int j = 0 ; j < aux ; ++j ){
            cin >> x;
            ++mp[x];
        }
        set<int>ans;
        for( map<int,int>::iterator it = mp.begin() ; it!=mp.end() ; ++it ){
            if((it -> second)%2 == 1) ans.insert(it -> first);
        }
        cout << "Case #"<<i<<":";
        for( set<int>::iterator ot = ans.begin() ; ot!= ans.end() ; ++ot ){
            cout << ' ' << *ot;
        } cout << '\n';
    }

}
