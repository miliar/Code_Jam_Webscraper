#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
vector<char> v,tt;

void shed(){
    for(ll i=v.size()-1;i>=0;i--){
        if(v[i]=='+'){
            v.pop_back();
        }
        else
            break;
    }
}

char neg(char a){
    return a=='+'?'-':'+';
}

ll cntl(){
    ll cnt=0;
    for(ll i=0;i<v.size();i++){
        if(v[i]=='+')
            cnt++;
        else
            break;
    }
    return cnt;
}

void flip(ll t){
    tt.clear();
    for(ll i=0;i<t;i++){
        tt.push_back(v[t-i-1]);
    }
    for(ll i=0;i<t;i++){
        v[i]=neg(tt[i]);
    }
}

void fun(){
    if(v.size()>0){
        if(v[0]=='-')
            flip(v.size());
        else
            flip(cntl());
    }
}

int main()
{
    ll tc;
    cin>>tc;
    for(ll t=1;t<=tc;t++){
        v.clear();
        string s;
        ll ans=0;
        cin>>s;
        for(ll i=0;i<s.length();i++){
            v.push_back(s[i]);
        }
        shed();
        while(v.size()>0){
            fun();
            shed();
            ans+=1;
        }
    //    flip(v.size());
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
