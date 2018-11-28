#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

int sum,ans;
int ca,cas;
char s[2000];
int i,j,n,x;

int main(){

  freopen("A-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  scanf("%d",&cas);
  for (ca=1;ca<=cas;ca++){
    sum=0;
    ans=0;
    memset(s,0,sizeof(s));
    scanf("%d%s",&n,s);
    for (i=0;i<=n;i++){
      ans+=max(0,(i-sum));
      sum+=max(0,(i-sum));
      sum+=(s[i]-'0');
    }
    printf("Case #%d: %d\n",ca,ans);


  }
  return 0;


}
