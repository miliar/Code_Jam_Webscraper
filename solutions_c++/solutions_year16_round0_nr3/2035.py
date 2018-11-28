#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<vector>
#include<fstream>
#define eps 1e-5
#define mod 1000000007
using namespace std;
int n,j;
int s[100];
long long gao(long long m,long long b){
    long long ans=0,b0=b,t;
    b=1;
    while(m){
        t=m&1ll;
        m/=10ll;
        ans+=b*t;
        b*=b0;
    }
    return ans;
};
void output()
{
    for(int i=1;i<=n;++i)cout<<s[i];for(int i=1;i<=n;++i)cout<<s[i];
    long long m=0;
    for(int i=1;i<=n;++i)m=m*10+s[i];
    for(int i=2;i<11;++i)
        cout<<" "<<gao(m,i);
    cout<<endl;
}
int main(){
    freopen("C-large.in.txt","r",stdin);
    freopen("c.out","w",stdout);
    cin>>n>>n>>j;
    cout<<"Case #1:\n";
    n/=2;
    for(int i=0;i<n;++i)s[i]=0;
    s[1]=s[n]=1;
    while(j--){
        output();
        s[2]+=1;
        for(int i=2;i<n;++i)
            if(s[i]>1){
                s[i+1]+=1;
                s[i]=0;
            }
    }
    return 0;
}