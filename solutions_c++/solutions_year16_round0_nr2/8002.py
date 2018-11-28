#include<bits/stdc++.h>

using namespace std;

#define LL long long
#define pb push_back
#define pLL pair<LL,LL>
#define ff first
#define ss second
#define rep(i,a,b) for(LL i=a;i<=b;++i)
#define ld double
#define mp make_pair
#define vLL vector<LL>
#define vpLL vector<pLL>
#define vld vector<ld>
#define pld pair<ld,ld>
#define vpld vector<pld>
#define SLL set<LL>
#define SpLL set<pLL>

LL t;
string str;
void rev(LL idx){
    string tmp;
    for(LL it=idx-1;it>=0;it--){
        if(str[it]=='+') tmp.pb('-');
        if(str[it]=='-') tmp.pb('+');
    }
    rep(it,0,idx-1) str[it]=tmp[it];
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    cin>>t;
    rep(loop,1,t){
        cin>>str;
        cout<<"Case #"<<loop<<": ";
        if(str.size()==1){
            if(str[0]=='+') cout<<0<<endl;
            else cout<<1<<endl;
            continue;
        }
        LL cnt=0,en=0;
        for(LL i=str.size()-1;i>=0;i--){
            if(str[i]=='+') en++;
            else break;
        }
        if(en==str.size()){
            cout<<0<<endl;
            continue;
        }
        if(str[0]=='-'){
            LL i;
            for(i=1;i<str.size();i++) if(str[i]!=str[i-1]) break;
            rev(str.size()-en);
            cnt+=1;
            en+=i;
        }
        while(en<str.size()){
            LL i;
            for(i=1;i<str.size();i++){
                if(str[i]!=str[i-1]) break;
            }
            rev(i);
            for(;i<str.size();i++){
                if(str[i]!=str[i-1]) break;
            }
            rev(str.size()-en);
            en+=i;
            cnt+=2;
        }
        cout<<cnt<<endl;
    }
}
