#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("cj.in","r",stdin);
    freopen("cj.out","w",stdout);
    int t; cin >> t;
    for(int tc=1 ; tc<=t ; tc++){
        int k,c,s; cin >> k >> c >> s;
        cout << "Case #" << tc << ": ";
        for(int i=1 ; i<k ; i++) cout << i << " ";
        cout << k << endl;
    }
    return 0;
}