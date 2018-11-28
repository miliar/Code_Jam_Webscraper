#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int tc, cases=1;
int maxr[110];
int maxc[110];
int map[110][110];     //r c n m
int n,m;

int main(){
  scanf("%d ",&tc);
  while(tc--){
    scanf("%d %d ",&n,&m);
    memset(maxr,0,sizeof(maxr));
    memset(maxc,0,sizeof(maxc));
    for(int i=0;i<n;i++) for(int j=0;j<m;j++){
      scanf("%d ",&map[i][j]);
      maxr[i]=max(maxr[i],map[i][j]);
      maxc[j]=max(maxc[j],map[i][j]);
    }
    bool ok = true;
    for(int i=0;i<n;i++) for(int j=0;j<m;j++)
            if((map[i][j]!=maxr[i]) && (map[i][j]!=maxc[j])) ok = false;
    if(ok) printf("Case #%d: YES\n",cases);
    else printf("Case #%d: NO\n",cases);
    cases++;
  }
  return 0;
}