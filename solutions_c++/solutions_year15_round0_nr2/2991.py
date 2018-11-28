#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int solve(vector<int> a,int n)
{
    sort(a.begin(),a.end(),greater<int>());
    int ans=a[0],cnt=0;
    if(a[0]<4) return a[0];
    for(int i=2;i<=a[0];i++){
            int cnt=0,j=0,mx=0;
            while(j<n&&a[j]>i){
            cnt+=a[j]/i;
            if(a[j]%i==0)cnt--;         
            j++;     
            }
            
           // printf("%d ::",cnt);
            cnt+=i;
           // printf("%d \n",i);
            ans=min(ans,cnt);
    }
return ans;
}
main()
{
      int n,t;
      int cas=1;
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
      cin>>t;
      while(t--){
      cin>>n;
      vector<int> v;
      for(int i=0;i<n;i++){ 
      int x;
      cin>>x;
      v.push_back(x);
      }
      printf("Case #%d: %d\n",cas++,solve(v,n));           
      }
      return 0;
}

