#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<iostream>
#include<algorithm>
#define ll long long
using namespace std;
vector<ll> list;
bool isPar(ll k){
    vector<int> v;
    while(k){
        v.push_back(k%10);
        k/=10;
    }
    int s=0,e=v.size()-1;
    while(s<e){
        if(v[s]!=v[e])return false;
        s++;e--;
    }
    return true;
}

void init(){
    for(int i=1;i<=1000000;i++){
        if(isPar(i)&&isPar(1LL*i*i))list.push_back(1LL*i*i);
    }
}
void solve(){
    ll a,b;
    cin >> a >> b;
    printf("%d\n", upper_bound(list.begin(),list.end(),b) - lower_bound(list.begin(),list.end(),a));
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    init();
    int n;
    scanf("%d",&n);
    for(int t=1;t<=n;t++){
        printf("Case #%d: ",t);
        solve();
    }
}
