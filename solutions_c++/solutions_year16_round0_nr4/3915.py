#include<bits/stdc++.h>
#define ll long long

using namespace std;

#define N   112345

int main(){
    #ifndef ONLINE_JUDGE
            freopen("D-small-attempt0.in","r",stdin);
            freopen("output.txt","w",stdout);
    #endif
    int t;
    cin >> t;
    for(int qq = 1; qq <= t; qq++){
        int k,c,s;
        cin >> k >> c >> s;
        printf("Case #%d: ",qq);
        for(int i = 1 ; i <= s ; i++){
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}
