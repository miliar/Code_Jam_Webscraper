#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<map>
#include<vector>
#include<deque>
using namespace std;
int t,m,n;
int arr[111][111];
int rowMax[111],colMax[111];
int main(){
  scanf("%d",&t);
  bool ok;
  for(int tc=1;tc<=t;tc++){
    ok=true;
    printf("Case #%d: ",tc);
    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++){
      rowMax[i]=-1;
      for(int k=0;k<m;k++){
        scanf("%d",&arr[i][k]);
        rowMax[i]=max(rowMax[i],arr[i][k]);
      }
    }
    for(int i=0;i<m;i++){
      colMax[i]=-1;
      for(int k=0;k<n;k++){
        colMax[i]=max(colMax[i],arr[k][i]);
      }
    }
    for(int i=0;i<n;i++){
      for(int k=0;k<m;k++){
        if(arr[i][k]==rowMax[i]||arr[i][k]==colMax[k])continue;
        ok=false;
        goto op;
      }
    }
    op:
    if(ok)printf("YES\n");
    else printf("NO\n");
  }
  return 0;
}
