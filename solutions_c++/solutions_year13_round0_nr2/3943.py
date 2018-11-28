#include <stdio.h>
#include <stdlib.h>

#define MAX_MN 100


int N,M;
int lawn[MAX_MN][MAX_MN];


int main()
{
  freopen("B-large.in","r",stdin);
  int T;
  scanf("%d\n",&T);
  for (int CASE = 1;CASE <= T;CASE++) {
    // read board
    scanf("%d %d",&N,&M);
    for (int i = 0;i < N;i++) {
      for (int j = 0;j < M;j++) {
        scanf("%d",&lawn[i][j]);
      }
    }

    //printf("yues\n");

    //check
    bool done;
    done = false;
    for (int i = 0;i < N;i++) {
      for (int j = 0;j < M;j++) {
        bool lh,rh,uh,dh;
        lh = rh = uh = dh = false;
        //left
        for (int k = 0;k < j;k++)
          if (lawn[i][k] > lawn[i][j]) { lh = true; break; }
        //right
        for (int k = j+1;k < M;k++)
          if (lawn[i][k] > lawn[i][j]) { rh = true; break; }
        //up
        for (int k = 0;k < i;k++)
          if (lawn[k][j] > lawn[i][j]) { uh = true; break; }
        //down
        for (int k = i+1;k < N;k++)
          if (lawn[k][j] > lawn[i][j]) { dh = true; break; }

        if ( (lh || rh) && (uh || dh) ) {
          printf("Case #%d: NO\n",CASE);
          done = true;
          break;
        }
      }
      if (done) break;;
    }
    if (!done) printf("Case #%d: YES\n",CASE);


  }
}
