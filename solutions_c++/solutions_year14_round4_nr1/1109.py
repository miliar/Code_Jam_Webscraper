#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int T,n,x,s[10001];
int chk[10001];
int cnt;

int main() {
  int i,j;
  scanf("%d",&T);
  for(int TT=1;TT<=T;TT++){
    scanf("%d%d",&n,&x);
    for(i=0;i<n;i++)scanf("%d",&s[i]);
    sort(s,s+n);
    memset(chk,0,sizeof(chk));
    cnt=0;
    for(i=n-1;i>=0;i--)if(!chk[i]){
      cnt++;
      chk[i]=1;
      for(j=i-1;j>=0;j--)if(!chk[j] && s[i]+s[j]<=x){
        chk[j]=1;
        break;
      }
    }
    printf("Case #%d: %d\n",TT,cnt);
  }
}
