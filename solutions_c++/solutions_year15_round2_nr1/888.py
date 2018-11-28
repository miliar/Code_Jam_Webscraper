#include<bits/stdc++.h>

using namespace std;


int rev(int k){
    int x = 0 ;
    while(k){
        x=x*10+(k%10);
        k/=10;
    }
    return x;

}

vector<int> ans;

void solve(){
    int n;
    cin >> n ;

    cout << ans[n] << endl;
}
void prep(){
    ans=vector<int> (1010000,10000000);
    ans[1]=1;
    for(int i =1 ; i <1000000;++i){
        ans[i+1]=min(ans[i+1],ans[i]+1);
        ans[rev(i)]=min(ans[rev(i)],ans[i]+1);
    }
}

int main(){
    prep();
    freopen("A-small-attempt1"".in","r",stdin);
    freopen("A-small-attempt1"".out","w",stdout);
    int T;
    cin >> T;
    for(int i = 1 ; i <= T ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
}
