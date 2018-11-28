#include<algorithm>
#include<cstdio>
#include<cstring>

using namespace std;

char s[110];
int i,j,k,n,m,ca,cas,ans,c;

int main(){

  freopen("B_l.in","r",stdin);
  freopen("B_l.out","w",stdout);
  scanf("%d",&cas);
  for (ca=1;ca<=cas;ca++){
    scanf("%s",s+1);
    n=strlen(s+1);
    ans=0;
    c=1;
    if (s[c]=='-'){
      while (c<=n && s[c]=='-') c++;
      ans=1;
    }
    while (1){
      while (c<=n && s[c]=='+') c++;
      if (c>n) break;
      while (c<=n && s[c]=='-') c++;
      ans+=2;
      if (c>n) break;
    }
    printf("Case #%d: %d\n",ca,ans);
  }

  return 0;



}
