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
        Int n,tmp;
        cin>>n;
        tmp=n;
        Int ans=1;
        bool visit[10];
        REP(i,10){
            visit[i]=false;
        }        
        if(n==0){
            cout<<"Case #"<<t<<": INSOMNIA"<<endl;
        }
        else{
            while(1){
                Int temp=n;
                while(temp>0){
                    if(visit[temp%10]==false){
                        visit[temp%10]=true;
                    }
                    temp=temp/10;
                }
                int f=0;
                REP(i,10){
                    if(visit[i]==false){
                        f=1;
                        break;
                    }
                }
                if(f==0){
                    cout<<"Case #"<<t<<": "<<n<<endl;
                    break;
                }
                else{
                    n+=tmp;
                    continue;
                }
            }
        }
    }
    return 0;
}
