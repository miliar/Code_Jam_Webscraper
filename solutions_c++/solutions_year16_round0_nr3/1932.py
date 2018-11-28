#include <bits/stdc++.h>

#define FOR(i,n) for(long long i=0;i<(long long)n;++i)
using namespace std;


string rev(string s){
    string ret="";
    for(int i=s.size()-1;i>=0;--i) ret=ret+s[i];

    return ret;
}

string tobinary(int x, int meret){
    string ret="";
    while(x!=0){
        if(x%2==1) ret+="1";
        else ret+="0";

        x/=2;
    }

    ret=rev(ret);

    while(ret.size()!=meret) ret="0"+ret;
    return ret;
}

int main(void){
    int t;cin>>t;
    int n,j;cin>>n>>j;

    cout<<"Case #1: "<<endl;

    int num=0;
    FOR(i,j){
        cout<<"1";
        cout<<tobinary(i,n/2-1);
        cout<<rev(tobinary(i,n/2-1));
        cout<<"1";

        cout<<" 3 4 5 6 7 8 9 10 11"<<endl;
    }
}
