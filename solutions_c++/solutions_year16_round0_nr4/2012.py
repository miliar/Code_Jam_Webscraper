#include<cstdio>
#include<cstring>
#include<queue>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<cmath>
#include<bitset>
#define rep(i,a,b) for(int i=a,_b=b;i<=_b;i++)
#define per(i,a,b) for(int i=a,_b=b;i>=_b;i--)
#define For(i,b) for(int i=0,_b=b;i<_b;i++)
#define upmax(a,b) if ((a)<(b)) (a)=(b)
#define upmin(a,b) if ((a)>(b)) (a)=(b)
using namespace std;

int T,K,C,S,n;
long long now;

int main(){
//freopen("D.in","r",stdin);
//freopen("D.out","w",stdout);
    cin>>T;
    rep(ca,1,T){
        cin>>K>>C>>S;
        cout<<"Case #"<<ca<<": ";
        n=(K-1)/C+1;
        if (n>S){
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        rep(i,1,n){
            now=1;
            rep(j,1,C){
                now=(now-1)*K+min((i-1)*C+j,K);
            }
            cout<<now<<' ';
        }
        cout<<endl;
    }
}