#include<bits/stdc++.h>
using namespace std;
string S,K;
int n;
set<string> M;
string res;
void dp(int pos, string L){
    if(L == K){
        M.insert(L);
        res = (*--M.end());
        return;
    }
    if(pos >= n){
        M.insert(L);
        return;
    }else{
        dp(pos+1,L + S[pos]);
        dp(pos+1,S[pos] + L);
    }
}
int main(){
    ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
    int t;
    cin>>t;
    for(int T = 1; T <= t; T++){
        cin>>S;
        K = S;
        n = S.size();
        string nu = "";
        dp(0,nu);
        cout<<"Case #"<<T<<": "<<res<<endl;
        M.clear();
    }
}
