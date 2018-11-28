#include <cstdlib>
#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

short mas[100][100];

int main(int argc, char *argv[])
{int T,N,M,L,i,j,x;
 freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
 scanf("%d",&T);
 for(L=1;L<=T;L++)
 {scanf("%d %d",&N,&M);
  vector<int>R(N,0),C(M,0);
  for(i=0;i<N;i++)
    for(j=0;j<M;j++)
    {scanf("%d",&x);
     mas[i][j]=x;
     if(x>R[i])R[i]=x;
     if(x>C[j])C[j]=x;
    }
  for(i=0;i<N;i++)
    for(j=0;j<M;j++)
    if(mas[i][j]<R[i] && mas[i][j]<C[j])goto LB;
  LB: printf("Case #%d: ",L);
      if(i<N)printf("NO\n");
      else printf("YES\n");
 }
//    system("PAUSE");
    return EXIT_SUCCESS;
}
