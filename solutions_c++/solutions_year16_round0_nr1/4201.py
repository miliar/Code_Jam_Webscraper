#include <bits/stdc++.h>
using namespace std;
int cnt[10];
bool ok(){
    for(int i = 0; i < 10; ++i){
        if(!cnt[i]) return false;
    }
    return true;
}
void countDigit(long long int x){
    do{
        ++cnt[x % 10];
        x /= 10;
    }while(x);
}
void solve(int n , int tc){
    if(!n){
        cout << "Case " << "#" << tc << ": INSOMNIA" << endl;
        return;
    }
    memset(cnt , 0 , sizeof cnt);
    countDigit(n);
    long long int x = n;
    while(!ok()){
      x += n;
      countDigit(x);
    }
    cout << "Case " << "#" << tc << ": " << x << endl;
 }
int main(){
    int tt;
    int n;
   // freopen("bal.txt" , "r" , stdin);
   // freopen("bal2.txt" , "w" , stdout);
    cin >> tt;
    int x = tt;
    while(tt--){
        cin >> n;
        solve(n , x - tt);
    }
    return 0;
}
