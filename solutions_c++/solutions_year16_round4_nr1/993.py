#include <bits/stdc++.h>
typedef __int128 INT;
typedef long long LL;
using namespace std;

istream& operator>>(istream& is,INT& x){
    LL _x;is>>_x;x=_x;return is;
}
ostream& operator<<(ostream& os,INT& x){
    os<<(LL)x;return os;
}
typedef vector<int> V;
typedef vector<V> VV;
string dfs(int sz,char result){
    if(sz==1){
        string res;
        res+=result;
        return res;
}
    string l,r;
    if(result=='R'){
        l=dfs(sz>>1,'R');
        r=dfs(sz>>1,'S');
    }
    if(result=='P'){
        l=dfs(sz>>1,'P');
        r=dfs(sz>>1,'R');
    }
    if(result=='S'){
        l=dfs(sz>>1,'S');
        r=dfs(sz>>1,'P');
    }
    if(l<r)return l+r;
    else return r+l;
}
void solve(){
    int t,R,P,S;
    cin>>t>>R>>P>>S;
    int n=R+P+S;
    {
        string a=dfs(n,'P');
        int r=0,p=0,s=0;
        for(int i = 0; i < n; i++){
            r+=(a[i]=='R');
            p+=(a[i]=='P');
            s+=(a[i]=='S');
        }
        if(r==R&&p==P&&s==S){
            cout <<a;
            return;
        }
    }
    {
        string a=dfs(n,'R');
        int r=0,p=0,s=0;
        for(int i = 0; i < n; i++){
            r+=(a[i]=='R');
            p+=(a[i]=='P');
            s+=(a[i]=='S');
        }
        if(r==R&&p==P&&s==S){
            cout <<a;
            return;
        }
    }
    {
        string a=dfs(n,'S');
        int r=0,p=0,s=0;
        for(int i = 0; i < n; i++){
            r+=(a[i]=='R');
            p+=(a[i]=='P');
            s+=(a[i]=='S');
        }
        if(r==R&&p==P&&s==S){
            cout <<a;
            return;
        }
    }
    cout<<"IMPOSSIBLE";
}

int main() {
    int T;cin>>T;
    for(int i = 1; i <= T; i++){
        cout<<"Case #"<<i<<": ";
        solve();
        cout<<endl;
    }

    return 0;
}
