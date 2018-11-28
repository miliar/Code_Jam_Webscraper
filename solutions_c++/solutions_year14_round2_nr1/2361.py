#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#include <iostream>
using namespace std;
#include <vector>

void go(vector <string> data,int k)
{
  int i,n= (int)data.size();
  vector <string> data_red;
  vector < vector <int> > Ns;
  char **reds = (char **)malloc(n*sizeof(char *));
  for(i=0;i<n;i++)
    {
      string cur = data[i];
      int l = cur.size();
      char *red = (char *)malloc(l+1);
      reds[i] = red;
      red[l] =0;
      int k = 0;
      red[k++] = cur[0];
      vector <int> NN;
      NN.push_back(0);
      int j;
      for(j=1;j<l;j++)
        {
          if (cur[j] != red[k-1])
            {
              red[k++]=cur[j];
              NN.push_back(0);
            }
          else
            NN[k-1]++;
        }
      Ns.push_back(NN);
      red[k]=0;
    }
  if (0)
    for(i=0;i<n;i++)
      {
        int j;
        printf("%s -->",data[i].c_str());
        printf("%s  ",reds[i]);
        for (j=0;j<Ns[i].size();j++)
          printf("%d ",Ns[i][j]);
        printf("\n");
      }
  string red0(reds[0]);
  for(i=1;i<n;i++)
    {
      //      if (strlen(reds[i]) != strlen(reds[0]))
      if (string(reds[i]) != red0)
        {
          printf("Case #%d: Fegla Won\n",k);
          return ;
        }
    }
  int nbc = Ns[0].size();
#define _ABS(x) ((x)<0 ? -(x) : (x))
  int ans = 0;
  for(i=0;i<nbc;i++)
    {
      int mi = 1000;
      int j,ma = 0;
      for(j=0;j<n;j++)
        {
          if (Ns[j][i]<mi)
            mi = Ns[j][i];
          if (Ns[j][i]>ma)
            ma = Ns[j][i];
        }
      int m,nb = 1000;
      for (m=mi;m<=ma;m++)
        {
          // on fait m
          int j,z = 0; 
          for(j=0;j<n;j++)
            z += _ABS(Ns[j][i]-m);
          if (z< nb)
            nb = z;
        }
      ans += nb;
      //printf("pour i= %d  nb = %d\n",i,nb);
    }
  printf("Case #%d: %d\n",k,ans);
}     // FIN go()
// ********************************************************

int main(int na,char *para[]) 
{
  int i,T;
  char line[6];

  fgets(line,6,stdin);
  sscanf(line,"%d",&T);
  for(i=0;i<T;i++)
    {
      fgets(line,6,stdin);
      int n;
      sscanf(line,"%d",&n);
      char line[256];
      vector <string> data;
      int k;
      for(k=0;k<n;k++)
        {
          fgets(line,256,stdin);
          line[strlen(line)-1] = 0;
          string st(line);
          data.push_back(st);
        }
      go(data,i+1);
    }

  return 0;
}		/* FIN main() */
/* *********************************************************** */
