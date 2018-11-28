/*
 *Written By: mkmishra1997
 *Note:       READ AT YOUR OWN RISK
 */
#include <bits/stdc++.h>
using namespace std;

typedef long long int   Int;
#define pii             pair<int,int> 
#define vi              vector<int>
#define pb(x)           push_back(x)
#define mp              make_pair
#define ff              first
#define ss              second
#define REP(i,n)        for(auto i=0; i<n ; i++)
#define FOR(i,a,b)      for(auto i=a; i<=b; i++)
#define RFOR(i,a,b)     for(auto i=a; i>=b; i--)
#define MOD             1000000007
#define bug(x)          cout<<">"<<#x<<" = "<<x<<endl

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t=1,T;
    cin>>T;
    for(;t<=T;t++){
        string s;
        cin>>s;
        int len=s.length();
        int ans=0;
        if(len==1){
            if(s.at(0)=='-'){
                ans=1;
            }
            else{
                ans=0;
            }
            cout<<"Case #"<<t<<": "<<ans<<endl;
            continue;
        }
        else{

            // int f=0,pos;
            // REP(k,len){
            //     FOR(j,k+1,len-1){
            //         if(s[k]!=s[j]){
            //             pos=j;
            //             REP(i,pos){
            //                 s[i]=s[pos];
            //             }
            //             ans++;
            //         }
            //     }
            // }
            // if(s[0]=='-'){
            //     ans++;
            // }
            int c1=0,c2=0;
            REP(i,len){
                if(s[i]=='-'){
                    c1=c1;
                }
                else{
                    c1=c2+1;
                }
                if(s[i]=='+'){
                    c2=c2;
                }
                else{
                    c2=c1+1;
                }
            }
            ans=min(c1+1,c2);
            cout<<"Case #"<<t<<": "<<ans<<endl;
        }
    }
    return 0;
}
