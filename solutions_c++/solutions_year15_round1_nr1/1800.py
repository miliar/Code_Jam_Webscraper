#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

int a[1100];
int i,j,n,ma,ans,ca,cas,a1,a2;

int main(){

  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  scanf("%d",&cas);
  for (ca=1;ca<=cas;ca++){
    memset(a,0,sizeof(a));
    ans=0;
    ma=0;
    scanf("%d",&n);
    for (i=1;i<=n;i++) scanf("%d",&a[i]);
    for (i=1;i<n;i++){
      ans+=max(0,a[i]-a[i+1]);
      ma=max(ma,max(0,a[i]-a[i+1]));
    }
    a1=ans;

    ans=0;
    for (i=1;i<n;i++){
      ans+=min(a[i],ma);
    }
    a2=ans;

    printf("Case #%d: %d %d\n",ca,a1,a2);

  }


  return 0;





}
