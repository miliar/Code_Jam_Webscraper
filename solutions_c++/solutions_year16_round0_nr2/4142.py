#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
int a=0;
char s[105],t[105];
int main(){
  int T,n,ca=0;
  freopen("a.txt","r",stdin);
  freopen("b.txt","w",stdout);
  scanf("%d",&T);
  while(T--){
    scanf("%s",s);
    int cnt=0;
    int n=strlen(s);
    for (int i=0;i<n;i++)
      if ((!i)||s[i]!=s[i-1]) cnt++;
    if (s[n-1]=='+') cnt--;
    printf("Case #%d: %d\n", ++ca,cnt);
  }
  return 0;
}