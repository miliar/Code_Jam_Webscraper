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

int T,n,k,cnt,a[11];

void check(int n){
    for(;n;n/=10){
        if (!a[n%10]){
            cnt--;
            a[n%10]=1;
        }
    }
}

int main(){
//freopen("A.in","r",stdin);
//freopen("A.out","w",stdout);
    cin>>T;
    rep(ca,1,T){
        For(i,10) a[i]=0;
        cin>>n;
        cout<<"Case #"<<ca<<": ";
        if (!n) {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        for(k=1,cnt=10;cnt;k++) check(k*n);
        cout<<(k-1)*n<<endl;
    }
}