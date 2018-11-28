#include<bits/stdc++.h>

using namespace std;


pair<bool,char> mul(pair<bool,char> a,pair<bool,char> b ){
    pair<bool,char> r;
    r.first= a.first^b.first;
    if(a.second=='1')r.second=b.second;
    else if(a.second==b.second){
        r.second='1';
        r.first=!r.first;
    }
    else if(a.second=='i'){
        if(b.second=='j')r.second='k';
        else{
            r.second = 'j';
            r.first=!r.first;
        }
    }
    else if ( a.second=='j'){
        if(b.second=='k'){
            r.second='i';
        }
        else {
            r.second='k';
            r.first=!r.first;
        }
    }
    else if(a.second=='k'){
        if(b.second=='i'){
            r.second='j';
        }
        else{
            r.second='i';
            r.first=!r.first;
        }
    }
    return r;
}

pair<bool,char> getSum(pair<bool,char> cur,long long p ){
    if(p==0)return {false,'1'};
    if(p==1)return cur;
    pair<bool,char> a = getSum(cur,p>>1);
    a=mul(a,a);
    if(p&1)a=mul(a,cur);
    return a;
}
void solve(){
    long long L,X;
    cin >>L >>X;
    string str;
    cin >> str;
    pair<bool,char > current = {false,'1'};

    pair<bool,char> cur ={false,'1'};
    for(int i = 0 ; i<L; ++i){
        pair<bool,char> b = {false,str[i%L]};
        cur=mul(cur,b);
    }

    int state=0;
    //pair<bool, char > = getSum(str,X);
    pair<bool,char> st1={false,'i'};
    pair<bool,char> st2={false,'k'};
    pair<bool,char> st3={true,'1'};
    for(long long i = 0 ; i < min(L*X,L*10) ; ++ i ){
        pair<bool,char> b = {false,str[i%L]};
        current=mul(current,b);
        if(state==0 &&current==st1)state=1;
        if(state==1 &&current==st2)state=2;
    }
    pair<bool,char> z = getSum(cur,X);
    //printf("%d %c\n",z.first,z.second);
    if(state==2 && getSum(cur,X)==st3){
        cout <<"YES"<<endl;
    }
    else cout<<"NO"<<endl;
}

int main(){
    freopen("C-large"".in","r",stdin);
    freopen("C-large"".out","w",stdout);
    int t;
    cin >> t;
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
}
