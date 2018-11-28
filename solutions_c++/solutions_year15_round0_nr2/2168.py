#include<cstdio>
#include<iostream> 
#include<cstring>
#include<string>
#include<set>
using namespace std;

int test,n,i,ans,tot,t,x,a[1005],j;
multiset<int> s;
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>test;
    for (t=1;t<=test;t++){
        cout<<"Case #"<<t<<": ";
        cin>>n;
        ans=0;
        for (i=1;i<=n;i++) cin>>a[i],ans=max(ans,a[i]);
        for (i=1;i<=ans;i++){
            tot=0;
            for (j=1;j<=n;j++) tot+=(a[j]-1)/i;
            ans=min(ans,tot+i);
        }
        cout<<ans<<endl;
    }
}
