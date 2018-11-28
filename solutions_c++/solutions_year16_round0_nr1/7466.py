#include<bits/stdc++.h>

using namespace std;

#define fin freopen("i1.in","r",stdin)
#define fout freopen("o1.out","w",stdout)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define fastio ios_base::sync_with_stdio(false); cin.tie(0);
#define ll long long

void getAns(ll n,ll test){
    set<ll> s;

    if(n==0){
        cout<<"Case #"<<test<<": "<<"INSOMNIA"<<endl;
        return;
    }
    ll no=n,i=1;
    while(s.size()!=10){
        no=n*i;
        i++;
        ll temp=no;
        while(temp>0) {
            s.insert(temp%10);
            temp/=10;
        }
    }
    cout<<"Case #"<<test<<": "<<no<<endl;
}

int main(){
    fin;
    fout;

    ll t;
    cin>>t;

    for(ll test=1;test<=t;test++){
        ll n;
        cin>>n;
        getAns(n,test);
    }

    return 0;
}
