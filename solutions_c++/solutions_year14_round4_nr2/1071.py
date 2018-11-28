#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#define N 1009
using namespace std;
int n,y[N],x[N];
void solve(){
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>x[i];
        y[i]=x[i];
    }
    sort(y,y+n);
    for(int i=0;i<n;i++){
        x[i]=lower_bound(y,y+n,x[i])-y;
    }
    int pos,ans=0,l=0,r=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)if(x[j]==i)pos=j;
        if(pos-l <= n-r-1-pos){
            while(pos!=l){
                swap(x[pos],x[pos-1]);
                pos--;
                ans++;
            }
            l++;
        }else{
            while(pos!=n-r-1){
                swap(x[pos],x[pos+1]);
                pos++;
                ans++;
            }
            r++;
        }
    }
    cout<<ans<<endl;
}
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;cin>>t;
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
