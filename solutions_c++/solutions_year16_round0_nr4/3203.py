#include <bits/stdc++.h>

using namespace std;

int T, k, c, s;
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin>>T;
    for(int t = 1; t <= T; ++t){
        cin>>k>>c>>s;
        cout<<"Case #"<<t<<": ";
        for(int i = 1; i <= s; ++i)
            cout<<i<<" ";
        cout<<endl;
    }
    return 0;
}
