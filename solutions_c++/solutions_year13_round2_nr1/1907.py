/*GCJ R1B A*/
#include<iostream>
#include<cmath>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstdlib>
using namespace std;
int T,ans,a,n;
int m[101],m1[101];
int sum[101];
int main(){
  cin>>T;
  for(int t=1;t<=T;t++){
    ans=0;
    cin>>a>>n;
    for(int i=0;i<n;i++){
      cin>>m[i];
    }
    sort(m,m+n);
    //cout<<"0k"<<endl;
    for(int i=0;i<n;i++){
      if(a>m[i]){
        a+=m[i];
        m1[i]=0;
        sum[i]=ans;
        //cout<<ans<<endl;
        continue;
      }
      if(a<=m[i]){
        if(a==1){
          ans+=n-i;
          goto END;
        }
        while(a<=m[i]){
          // cout<<a<<" "<<m[i]<<endl;
          a+=a-1;
          ans++;
        }
        a+=m[i];
      }
      sum[i]=ans;
      //cout<<ans<<endl;
    }
    for(int i=0;i<n;i++){
      //cout<<ans<<endl;
      ans=min(ans,(((i!=0)?sum[i-1]:0)+n-i));    
    }
  END:
    printf("Case #%d: %d\n",t,(int)ans);
  }
}
