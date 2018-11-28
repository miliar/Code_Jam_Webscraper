#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T,C=1,n,m,maior;
int want[128][128];
int curr[128][128];
bool res;

void print(){
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++)
      printf("%d ",curr[i][j]);
    printf("\n");
  }
  printf("\n");
}

int main(){

  scanf("%d",&T);
  while(T--){
    printf("Case #%d: ",C++);
    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++){
        scanf("%d",&(want[i][j]));
        curr[i][j] = 100;
      }

    // rows
    for(int i=0;i<n;i++){
      maior = want[i][0];
      for(int j=1;j<m;j++)
        maior = max(maior,want[i][j]);

      // cut
      for(int j=0;j<m;j++)
        if(curr[i][j]>maior)
          curr[i][j]=maior;
      //print();
    }

    // cols
    for(int j=0;j<m;j++){
      maior = want[0][j];
      for(int i=1;i<n;i++)
        maior = max(maior,want[i][j]);

      // cut
      for(int i=0;i<n;i++)
        if(curr[i][j]>maior)
          curr[i][j]=maior;
      //print();
    }

    res=true;
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++)
        if(curr[i][j]!=want[i][j])
          res=false;
    printf("%s\n",res?"YES":"NO");
  }

  return 0;
}
