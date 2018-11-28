#include <bits/stdc++.h>
using namespace std;
char cnt[2000];
int n,t;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int cs=1;cs<=t;cs++){
        memset(cnt,0,sizeof cnt);
        cin>>n;
        cin>>cnt;
        for(int i=0;i<=n;i++){
            cnt[i]-='0';
        }
        int ans =0,total=0;
        for(int i=0;i<=n;i++){
            //cout<<i<<total<<ans<<endl;
            if(cnt[i]>0){
                if(total >= i){
                    total += cnt[i];
                }else{
                    int add = i - total;
                    ans += add;
                    total += add + cnt[i];
                }
            }
        }
        cout<<"Case #"<<cs<<": "<<ans<<endl;
    }
}
