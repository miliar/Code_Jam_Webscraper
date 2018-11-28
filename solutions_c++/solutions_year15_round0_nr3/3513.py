#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define F first
#define S second
using namespace std;
pair<char,bool> mul(char a,char b){
    if(a=='1')return mp(b,false);
    if(b=='1')return mp(a,false);
    if(a=='i'){
        if(b=='i'){
            return mp('1',true);
        }else if(b=='j'){
            return mp('k',false);
        }else if(b=='k'){
            return mp('j',true);
        }
    }else if(a=='j'){
        if(b=='i'){
            return mp('k',true);
        }else if(b=='j'){
            return mp('1',true);
        }else if(b=='k'){
            return mp('i',false);
        }
    }else if(a=='k'){
        if(b=='i'){
            return mp('j',false);
        }else if(b=='j'){
            return mp('i',true);
        }else if(b=='k'){
            return mp('1',true);
        }
    }
}
int main(){
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int T,l,I,K;
    long long x=1;
    cin>>T;
    for(int t=1;t<=T;++t){
        string s;
        cin>>l>>x;
        cin>>s;
        string ts=s;
        for(int i=1;i<x;++i)s+=ts;
//        cout<<s<<endl;
        char tmp=s[0];
        bool sign =false;
        int f=0;
        pair<char,bool>p;
        if(tmp=='i'){f++; I=1;goto ifound;}
        for(int i=1;i<s.size();++i){
            if(tmp=='i'){
                I=i;
                f++;
                goto ifound;
            }
            p=mul(tmp,s[i]);
            tmp=p.F;
            if(sign) sign^=p.S;
            else sign|=p.S;
        }
        ifound:;
        tmp=s[s.size()-1];
        if(tmp=='k'){f++; K=s.size()-2; goto kfound;}
        for(int i=s.size()-2;i>I;--i){
            if(tmp=='k'){
                K=i;
                f++;
                goto kfound;
            }
            p=mul(s[i],tmp);
            tmp=p.F;
            if(sign) sign^=p.S;
            else sign|=p.S;
        }
        kfound:;
        tmp=s[I];
        for(int i=I+1;i<=K;++i){
            p=mul(tmp,s[i]);
            tmp=p.F;
            if(sign) sign^=p.S;
            else sign|=p.S;
        }
        if(tmp=='j'){
                f++;
        }
        cout<<"Case #"<<t<<": ";
        if(f==3&&(!sign))cout<<"YES";
        else cout<<"NO";
        cout<<endl;
    }
}

