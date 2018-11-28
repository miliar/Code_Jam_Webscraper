#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#define PB push_back
#define FT first
#define SD second
#define MP make_pair
using namespace std;
int a[1005];
int main()
{
         freopen("A-large.in","r",stdin);
         freopen("A-large.out","w",stdout);
         int T,ca=0;
         scanf("%d",&T);
         while(T--){
                  int n;
                  scanf("%d",&n);
                  for(int i=1;i<=n;i++)
                           scanf("%d",&a[i]);
                  int ans1=0,ans2=0;
                  int _max=0;
                  for(int i=2;i<=n;i++){
                           if(a[i]<a[i-1]) {
                                             ans1+=a[i-1]-a[i];
                                             _max=max(_max,a[i-1]-a[i]);
                           }
                  }
                  //cout<<_max<<endl;
                  for(int i=1;i<=n-1;i++){
                                    if(a[i]>=_max) ans2+=_max;
                                    else ans2+=a[i];
                  }
                  printf("Case #%d: %d %d\n",++ca,ans1,ans2);
         }
         return 0;
}
