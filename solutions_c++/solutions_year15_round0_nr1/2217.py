#include<cstdio>
#include<iostream> 
#include<cstring>
#include<string>
using namespace std;

int test,n,i,a[100005],sum[100005],tot,t;
string s;

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>test;
    for (t=1;t<=test;t++){
          cout<<"Case #"<<t<<": ";
          cin>>n;
          cin>>s;
          sum[0]=0;
          for (i=1;i<=n+1;i++) a[i]=s[i-1]-'0',sum[i]=sum[i-1]+a[i];
          tot=0;
          for (i=1;i<=n+1;i++){
              if (sum[i]+tot<i) tot+=i-(sum[i]+tot);
          }
          cout<<tot<<endl;
          
    }
}
