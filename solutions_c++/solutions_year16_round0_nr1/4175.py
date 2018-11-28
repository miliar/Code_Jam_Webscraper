#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define all(a)  (a).begin(),(a).end()
#define vi vector<int>
#define pb push_back
#define INF 999999999

bool isAllTrue(vector<bool> used){
    rep(i,10)if(used[i]==false)return false;
    return true;
}

void check(vector<bool> &used,ll tmp){
    while(tmp){
        int num = tmp%10;
        used[num]=true;
        tmp/=10;
    }
}

ll solve(ll n){
    vector<bool> used(10,false);
    
    rep(i,1e5){
        ll tmp = i*n;
        check(used,tmp);
        if(isAllTrue(used))return tmp;
    }
    return -1;
}


int main(){
    int t;
    cin>>t;
    rep(i,t){
        ll n;
        cin>>n;
        int res = solve(n);
        cout<<"Case #"<<i+1<<": ";
        if(res==-1)cout<<"INSOMNIA"<<endl;
        else cout<<res<<endl;
    }
}