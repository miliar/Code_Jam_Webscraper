#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define F first
#define S second
using namespace std;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,sm,ans=0,clap=0;
    string s;
    cin>>T;
    for(int t=1;t<=T;t++){
        cin>>sm;
        cin>>s;
        clap=0;
        ans=0;
        for(int i=0;i<=sm;++i){
            if(clap<i){
                ans+=i-clap;
                clap=i;
            }
            clap+=(s[i]-'0');

        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
}

