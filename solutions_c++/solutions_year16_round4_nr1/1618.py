#include <bits/stdc++.h>
#define F(n) Fi(i,n)
#define Fi(i,n) Fl(i,0,n)
#define Fl(i,l,n) for(int i=l;i<n;i++)
using namespace std;
char win(char a, char b){
    if(a>b)swap(a,b);
    if(a=='P'&&b=='R')return 'P';
    if(a=='P'&&b=='S')return 'S';
    if(a=='R'&&b=='S')return 'R';
    assert(false);
}
bool check(string s){
    string s2;
    if(s.size()==1)return true;
    F(s.size()/2){
        if(s[i*2] == s[i*2+1])return false;
        s2 += win(s[i*2],s[i*2+1]);
    }
    return check(s2);
}
main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t, r,p,s;
    cin>>t;
    Fl(_,1,t+1){
        cout<<"Case #"<<_<<": ";
        cin>>r>>r>>p>>s;
        string tmp;
        F(p)tmp+='P';
        F(r)tmp+='R';
        F(s)tmp+='S';
        bool hasans = false;
        // cout<<tmp<<' '<<r<<' '<<p<<' '<<s<<endl;
        do{
            if(check(tmp)){
                cout<<tmp<<endl;
                hasans = true;
                break;
            }
        }while(next_permutation(tmp.begin(),tmp.end()));
        if(!hasans)cout<<"IMPOSSIBLE"<<endl;
    }
}