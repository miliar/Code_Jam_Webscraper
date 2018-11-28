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

int T,n,ans,a[1200];
string s;

int main(){
//freopen("B.in","r",stdin);
//freopen("B.out","w",stdout);
    cin>>T;
    rep(ca,1,T){
        cin>>s;
        a[n=0]=-1;
        ans=0;
        cout<<"Case #"<<ca<<": ";
        For(i,s.size()){
            a[++n]=(s[i]=='+');
            if (a[n]==a[n-1]) n--;
        }
        rep(i,1,n) if (!a[i]){
            ans+=(i==1?1:2);
        }
        cout<<ans<<endl;
    }
}