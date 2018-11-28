#include <bits/stdc++.h>
using namespace std;
int t,l,x;
string s;
struct Num{
    int val;
    int tag;
    Num(const string& s,int pos){
        char c = s[pos];
        if(c=='i'){
            this->val=1;
        }else if(c=='j'){
            this->val=2;
        }else if(c=='k'){
            this->val=3;
        }else{
            cerr<<"error"<<c<<endl;
        }
        tag = 1;
    }

    Num(int val=0){
        this->val = val;
        tag = 1;
    }
    Num operator*(const Num& r)const {
        static int ans[4][4] = {
            {
                0,1,2,3
            },
            {
                1,0,3,2
            },
            {
                2,3,0,1
            },
            {
                3,2,1,0
            }
        };
        static int tags[4][4] ={
            {
                1,1,1,1
            },
            {
                1,-1,1,-1
            },
            {
                1,-1,-1,1
            },
            {
                1,1,-1,-1
            }
        };
        Num ret(ans[val][r.val]);
        ret.tag = tag * r.tag * tags[val][r.val];
        return ret;
    }
    bool operator==(const Num&r)const{
        return val == r.val && tag == r.tag;
    }
}dp[20000];
int main(){
#define RUN
#ifdef RUN
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif // RUN
    cin>>t;
    for(int cs=1;cs<=t;cs++){
        cin>>l>>x;
        string ts;
        cin>>ts;
        s="";
        for(int i=0;i<x;i++)
            s+=ts;
        dp[l*x] = Num(0);
        for(int i=l*x-1;i>=0;i--){
            dp[i] =  Num(s,i) * dp[i+1] ;
        }
        Num tmp(s,0);
        bool ok = false;
        bool hasi = (tmp == Num(1));
        for(int i=1;i<l*x;i++){
            if(hasi && tmp==Num(3) && dp[i]==Num(3)){
                ok = true;
                break;
            }
            tmp = tmp*Num(s,i);
            hasi |= (tmp==Num(1));
        }
        cout<<"Case #"<<cs<<": "<<(ok?"YES":"NO")<<endl;
    }
}
