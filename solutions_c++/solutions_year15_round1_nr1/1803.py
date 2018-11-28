#include <bits/stdc++.h>
using namespace std;
int t,m;
typedef long long ll;
ll a[2000];
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int cs=1;cs<=t;cs++){
       cin>>m;
       for(int i=0;i<m;i++){
        cin>>a[i];
       }
       ll ans1=0,ans2=0;
       ll rate = 0;
       for(int i=0;i<m-1;i++){
            if(a[i+1]<a[i]){
                ll dif = a[i]-a[i+1];
                ans1 += dif;
                if(dif > rate)
                    rate = dif;
            }
       }
       for(int i=0;i<m-1;i++){
            if(a[i] < rate){
                ans2 += a[i];
            }else{
                ans2+=rate;
            }
       }
       cout<<"Case #"<<cs<<": "<<ans1<<" "<<ans2<<endl;

    }
}
