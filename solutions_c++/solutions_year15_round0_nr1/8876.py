#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#define rep(i,a,n) for(int i=a,_n=n;i<=_n;i++)
#define per(i,a,n) for(int i=a,_n=n;i>=_n;i--)
#define For(i,n) for(int _n=n,i=0;i<_n;i++)
#define pii pair<int,int>
#define FI first
#define SE second
#define tget(a,b) if ((b)<(a)) (a)=(b);
using namespace std;
typedef long long ll;

int cas,n,ans,k;
char ch;

int main(){
ios::sync_with_stdio(false);
//freopen("a.in","r",stdin);
//freopen("a.out","w",stdout);
    cin>>cas;
    rep(ca,1,cas){
        cin>>n;
        ans=k=0;
        rep(i,0,n){
            if (k<i){
                ans+=i-k;
                k=i;
            }
            cin>>ch;
            k+=ch-'0';
        }
        cout<<"Case #"<<ca<<": "<<ans<<endl;
    }
}





















