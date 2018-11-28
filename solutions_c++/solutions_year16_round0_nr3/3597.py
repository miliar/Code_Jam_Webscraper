#include "bits/stdc++.h"
#include <cassert>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define all(a)  (a).begin(),(a).end()
#define vi vector<int>
#define pb push_back
#define int ll
#define INF 999999999



int to10(int n,int num){
    string s = "";
    rep(i,n){
        s+='0'+(num%2);
        num/=2;
    }
    reverse(all(s));
    return stoll(s);
}


int inter(int num,int base){
    stringstream ss;
    ss<<num;
    string s=ss.str();
    
    int ret = 0;
    rep(i,s.size()){
        ret*=base;
        ret+=s[i]-'0';
    }
    return ret;
}

int yaku(int n){
    for(int i=2;i<n;i++){
        if(n%i==0)return i;
    }
    assert(false);
}

bool isp(int n){
    if(n==1)return false;
    if(n==2)return true;
    for(int i=2;i*i<=n;i++){
        if(n%i==0)return false;
    }
    return true;
}



bool solve(int n,int num){
    vector<int> number(11);
    number[2] = num;
    if(isp(number[2]))return false;
    
    number[10]=to10(n,num);
    if(isp(number[10]))return false;
    
    for(int i=3;i<=9;i++){
        number[i] = inter(number[10],i);
        if(isp(number[i]))return false;
    }

    cout<<number[10];
    for(int i=2;i<=10;i++){
        cout<<" "<<yaku(number[i]);
    }
    
    cout<<endl;
    return true;
}
signed main(){
    
    int t;
    cin>>t;
    rep(loop,t){
        int n,j;
        cin>>n>>j;
        cout<<"Case #"<<loop+1<<":"<<endl;
        
        int start = 1;
        rep(i,n-1)start*=2;
        for(int i=start;i<(1<<n);i++){
            if(i%2==0)continue;
            if(solve(n,i)){
                j--;
            }
            if(j==0)break;
        }
    }
}


