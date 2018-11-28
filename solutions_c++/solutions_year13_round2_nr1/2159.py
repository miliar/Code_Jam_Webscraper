# include <cstdio>
# include <algorithm>
# include <cstring>
using namespace std;

# define normalise(a) if(a>ar[N-1])a=ar[N-1]+1
int maxsize[101][101];
int ar[100];

int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
  {
    int A,N;
    scanf("%d%d",&A,&N);
    for(int i=0;i<N;i++)
      scanf("%d",ar+i);
    sort(ar,ar+N);

    memset(maxsize,0,101*101*4);
    maxsize[0][0]=A;
    for(int i=1;i<=N;i++)
    {
      maxsize[0][i]=maxsize[0][i-1]*2-1;
      normalise(maxsize[0][i]);
    }

    for(int i=0;i<N;i++)
    {
      for(int j=0;j<=N;j++)
      {
        if(maxsize[i][j]==0)continue;

        if(maxsize[i][j]>ar[i])
        {
          maxsize[i+1][j]=max(maxsize[i+1][j],maxsize[i][j]+ar[i]);
          normalise(maxsize[i+1][j]);
          for(int k=j+1;k<=N;k++)
          {
            maxsize[i+1][k]=max(maxsize[i+1][k],2*maxsize[i+1][k-1]-1);
            normalise(maxsize[i+1][k]);
          }
        }
        else
        {
          maxsize[i+1][j+1]=max(maxsize[i+1][j+1],maxsize[i][j]);
          normalise(maxsize[i+1][j+1]);
          for(int k=j+2;k<=N;k++)
          {
            maxsize[i+1][k]=max(maxsize[i+1][k],2*maxsize[i+1][k-1]-1);
            normalise(maxsize[i+1][k]);
          }
        }
      }
    }

    for(int i=0;i<=N;i++)
    {
      if(maxsize[N][i]>0)
      {
        printf("Case #%d: %d\n",t,i);
        break;
      }
    }
  }
  return 0;
}
