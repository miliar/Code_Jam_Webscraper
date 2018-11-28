#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<assert.h>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<limits.h>

using namespace std;

#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define EPS 1e-9
#define asdf exit(0);
#define AB(a) ((a)<(0) ? (-(a)) : (a))
#define EQ(a,b) ( (fabs((a)-(b))<EPS) ? (1) : (0))




typedef long long LL;
//typedef __int64 LL;

int n;
int mat2[4][4];
int mult[8][8];


int get(int a,int b)
{
  int ret=1;
  if(a>=4)
  {
    a-=4;
    ret*=-1;
  }
  if(b>=4)
  {
    b-=4;
    ret*=-1;
  }


  int temp=mat2[a][b];
  if(ret<0)
  {
    if(temp>=4)
    {
      temp-=4;
      ret=temp;
    }
    else
    {
      ret=temp+4;
    }
    return ret;
  }
  else return mat2[a][b];
}



void pre()
{
  int i,j;
  mat2[0][0]=0;
  mat2[0][1]=1;
  mat2[0][2]=2;
  mat2[0][3]=3;

  mat2[1][0]=1;
  mat2[1][1]=4;
  mat2[1][2]=3;
  mat2[1][3]=6;

  mat2[2][0]=2;
  mat2[2][1]=7;
  mat2[2][2]=4;
  mat2[2][3]=1;

  mat2[3][0]=3;
  mat2[3][1]=2;
  mat2[3][2]=5;
  mat2[3][3]=4;

  for(i=0;i<8;i++)
  for(j=0;j<8;j++)
    mult[i][j]=get(i,j);
}




char in[1000010];



int L[1000010];
int R[1000010];



int pow(long long val)
{
  if(val==0) return 0;
  int ret=pow(val/2);
  ret=mult[ret][ret];
  if(val%2)
    ret=mult[ret][L[n-1]];
  return ret;
}



int rest(long long lastVals)
{
  long long divider=n;
  int now=pow(lastVals/divider);
  lastVals%=divider;
  now=mult[R[n-lastVals]][now];
  return now;
}



int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int i,j,k,repeat;
    int T;

    pre();

    scanf("%d",&T);
    for(int cs=1;cs<=T;cs++)
    {
      int ok=0;

      scanf("%d %d",&n,&repeat);
      scanf("%s",in);

      long long UpLim=((LL)n)*((LL)repeat);

      if(n==1)
      {
        printf("Case #%d: NO\n",cs);
        continue;
      }

      L[0]=in[0]-'i'+1;
      for(i=1;i<n;i++)
      {
        L[i]=mult[L[i-1]][in[i]-'i'+1];
      }


      R[n]=0;
      for(i=n-1;i>=0;i--)
      {
        R[i]=mult[in[i]-'i'+1][R[i+1]];
      }

      long long inf=1000000000;
      inf*=inf;

      long long minIpos=inf;

      for(i=0;i<n;i++)
      {
        int now=L[i];
        int gunFactor=mult[R[i+1]][L[i]];
        LL nowPos=i;
        if(now==1)//i
        {
          minIpos=nowPos;
          break;
        }

        for(j=1; (nowPos+n)<UpLim && j<=10;j++)
        {
          nowPos+=n;
          now=mult[now][gunFactor];

          if(now==1)//i
          {
            minIpos=min(nowPos,minIpos);
          }
        }
      }

      if(minIpos==inf)
      {
        printf("Case #%d: NO\n",cs);
        continue;
      }


      for(i=0;i<n;i++)
      {
        int now=L[i];
        int gunFactor=mult[R[i+1]][L[i]];
        int nowPos=i;

        for(j=1; (nowPos)<UpLim && j<=80;j++)
        {
          if (nowPos > minIpos && now == 3 && rest(UpLim - nowPos - 1) == 3)  //j
          {
            ok = 1;
          }
          nowPos+=n;
          now=mult[now][gunFactor];
        }
      }



      if(ok) printf("Case #%d: YES\n",cs);
      else printf("Case #%d: NO\n",cs);
    }



    return 0;
}
