#include<iostream>
#include<stdio.h>

using namespace std;

int all(string s){
    int l = s.size();
    for(int i=0;i<l;i++) if(s[i]!='+') return 0;
    return 1;
}

int check(string s){
    if(all(s)) return 0;
    int l =s.size();
    int cnt = 1;
    char c = s[0];
    for(int i=1;i<l;i++){
        if(c != s[i]){
            cnt++;
            c = s[i];
        }
    }
    if(c=='+') cnt=cnt-1;
    return cnt;
}

int main(){
    int t;
    freopen("B-large.txt","r",stdin);
    freopen("out.txt","w",stdout);
    string s;
    cin>>t;
    for(int cas=1;cas<=t;cas++){
        cin>>s;
        cout<<"Case #"<<cas<<": ";
        cout<<check(s)<<endl;
    }
}
