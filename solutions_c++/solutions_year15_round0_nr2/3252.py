#include<cstdio>
#include<algorithm>
#include<cstring>
#include<queue>

using namespace std;

int a[1100];
int i,j,k,ca,cas,t,num,ans,n;

int Work(int t){

int c,d,i;

  d=0;
  c=0;

  for (i=1;i<=n;i++){
    if (a[i]>t){
      c+=a[i]/t;
      if (a[i] % t==0) c--;
    }
    else d=max(d,a[i]);
  }

  return c+max(t,d);


}



int main(){

  freopen("B-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  scanf("%d",&cas);
  for (ca=1;ca<=cas;ca++){
    memset(a,0,sizeof(a));
    num=0;
    ans=9999999;
    scanf("%d",&n);
    for (i=1;i<=n;i++) {
      scanf("%d",&a[i]);
      num=max(num,a[i]);
    }
    for (t=num;t>0;t--){
      ans=min(ans,Work(t));
   //   printf("%d\n",Work(t));
    }

    printf("Case #%d: %d\n",ca,ans);


  }

  return 0;


}
