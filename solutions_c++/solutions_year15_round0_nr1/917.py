#include<bits/stdc++.h>


using namespace std;


void solve(){
    int mx;
    string str;
    cin >> mx >> str;
    int cum=0;
    int toAdd=0;
    for(int i = 0 ; i <= mx ; ++ i ){
        if(cum<i){
            toAdd+=i-cum;
            cum=i;
        }
        cum+=str[i]-'0';
    }
    cout << toAdd << endl;
}

int main(){
    freopen("A-large"".in","r",stdin);
    freopen("A-large"".out","w",stdout);
    int t;
    cin >> t;
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
