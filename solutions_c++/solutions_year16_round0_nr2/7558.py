#include<bits/stdc++.h>

using namespace std;

#define fin freopen("i1.in","r",stdin)
#define fout freopen("o1.in","w",stdout)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define fastio ios_base::sync_with_stdio(false); cin.tie(0);
#define ll long long
#define oo(x) do{ for(int zo=1;zo<=5;zo++) cout<<x; cout<<"\n"; }while(0);

ll getAns(string s){
    ll ans=0;

    string dir="left";
    ll i=0;
    ll j=s.length()-1;

    while(i<=j){
        if(dir=="left"){
            while(i<=j && s[j]=='+')
                j--;
            if(i<=j && s[j]=='-'){
                ans++;
                while(i<=j && s[j]=='-'){
                    j--;
                }
            }
            dir="right";
        }
        else {
            while(i<=j && s[j]=='-')
                j--;
            if(i<=j && s[j]=='+'){
                ans++;
                while(i<=j && s[j]=='+'){
                    j--;
                }
            }
            dir="left";
        }
    }

    return ans;
}

int main(){

    fin;
    fout;

    ll t;
    cin>>t;

    for(ll test=1;test<=t;test++){
        string s;
        cin>>s;
        cout<<"Case #"<<test<<": "<<getAns(s)<<endl;
    }

    return 0;
}
