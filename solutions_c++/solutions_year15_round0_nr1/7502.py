#include <iostream>
#include <algorithm>
using namespace std;
int S[1005];

int main(){

    int t, n;
    string st;
    cin>>t;

    for(int k = 1; k <= t; k++){
        cin>>n>>st;
        int ans = 0, total = 0;
        for(int i = 0; i <= n; i++){
            int s = st[i] - '0';
            if(i > total && s > 0){
                ans += (i - total);
                total += (i - total);
            }
            total += s;
            // cout<<i<<" "<<ans<<" "<<total<<endl;
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
}