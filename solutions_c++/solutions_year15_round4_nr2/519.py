#include<bits/stdc++.h>
#define next sled
#define pb push_back
#define ld long double
const int N=120000;
using namespace std;
int n;
ld b[40],a[40],x,r,q,w,l,ans;
int tek1;
main(){
    cin.tie(0);ios_base::sync_with_stdio(0);
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    cin>>tek1;
    for(int tt=1;tt<=tek1;++tt){

      cout.precision(9);
      cin>>n>>x>>r;
      for(int i=1;i<=n;++i)
        cin>>a[i]>>b[i];
      //  cout<<tt<<' '<<n<<' '<<x<<' '<<r<<endl;
      //  cout<<a[1]<<' '<<b[1]<<endl;
      //  if(n==2)cout<<a[2]<<' '<<b[2]<<endl;
    cout<<"Case #"<<tt<<": ";
    if(n==2&&b[1]==b[2]){
        a[1]+=a[2];
        n=1;
    }
      if(n==1){
        if(b[1]==r){
            ans=(x/a[1]);
            cout<<fixed<<ans;
            cout<<"\n";
        }else cout<<"IMPOSSIBLE\n";
        continue;
      }
      if((max(b[1],b[2])<r)||(min(b[1],b[2])>r)){
        cout<<"IMPOSSIBLE\n";
        continue;
      }
      q=(b[1]-b[2]);
      w=(r*x-x*b[2]);
      l=(w/q);
      ans=max(l/a[1],(x-l)/a[2]);
      cout<<fixed<<ans;
      cout<<"\n";
    }

}
