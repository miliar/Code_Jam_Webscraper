#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

FILE *f1=fopen("A-small-attempt0.in","r");
FILE *f2=fopen("A-small-attempt0.out","w");

int t,vis[17],n,map[5][5],flag,ans;

int main(int argc, char *argv[])
{
    fscanf(f1,"%d",&t);
    for(int k=1;k<=t;k++)
    {
      memset(vis,0,sizeof(vis));flag=0;
      fscanf(f1,"%d",&n);
      for(int i=1;i<=4;i++)for(int j=1;j<=4;j++)fscanf(f1,"%d",&map[i][j]);
      for(int i=1;i<=4;i++)vis[map[n][i]]++;
      fscanf(f1,"%d",&n);
      for(int i=1;i<=4;i++)for(int j=1;j<=4;j++)fscanf(f1,"%d",&map[i][j]);
      for(int i=1;i<=4;i++)vis[map[n][i]]++;
      for(int i=1;i<=16;i++)
      {
        if(vis[i]>1)
        {
          flag++;
          ans=i;
        }
      }
      fprintf(f2,"Case #%d: ",k);
      if(flag==0)fprintf(f2,"Volunteer cheated!\n");
      else if(flag==1)fprintf(f2,"%d\n",ans);
      else fprintf(f2,"Bad magician!\n");
    }
    return 0;
}
