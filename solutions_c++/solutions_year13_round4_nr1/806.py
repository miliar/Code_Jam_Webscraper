#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<vector>
#include<stdlib.h>
#include<time.h>
#define MOD 1000002013
#define INF 1999999999
using namespace std;
int T,n,m;
long long a1[1000111],a2[1000111];
int A=0;
struct Node
{
  long long x,y,p;
};
long long b[1000111];
int B=0;
Node in[1000111];
long long cal(long long xx,long long yy,long long p)
{
 // printf(">>> %I64d %I64d %I64d\n",xx,yy,p);
  long long t,tt,ttt;
  t=yy-xx;
  tt=t*n;
  ttt=(t*(t-1))/2;
  tt%=MOD;
  ttt%=MOD;
  tt-=ttt;
  if(tt<=0)tt+=MOD;
  if(tt<=0)tt+=MOD;
  tt%=MOD;
  tt*=p;
  tt%=MOD;
  return tt;
}
int main()
{

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    int i,j,k;
    int q,r;
    long long t,tt,ttt,ff;
    long long aa,bb;
    scanf("%d",&T);
for(int ii=1;ii<=T;ii++)
 {
  scanf("%d %d",&n,&m);
  aa=0;bb=0;A=0;B=0;
  for(i=0;i<m;i++)
   {
     scanf("%I64d %I64d %I64d",&in[i].x,&in[i].y,&in[i].p);
     t=in[i].y-in[i].x;
     tt=t*n;
     tt%=MOD;
     ttt=(t*(t-1))/2;
     ttt%=MOD;
     tt-=ttt;
     if(tt<=0)tt+=MOD;
     if(tt<=0)tt+=MOD;
     tt%=MOD;
     tt*=in[i].p;
     tt%=MOD;
     aa+=tt;
     aa%=MOD;
     b[B]=in[i].x;
     B++;
     b[B]=in[i].y;
     B++;
   }
  sort(b,b+B);
  for(i=1;i<B;i++)
   {
     if(b[i]==b[i-1])b[i-1]=INF;
   }
  k=0;
  for(i=0;i<B;i++)
   {
     if(b[i]!=INF)
      {
        b[k]=b[i];
        k++;
      }
   }
  B=k;
  //printf("><\n");
  //for(i=0;i<B;i++)printf("%I64d ",b[i]);printf("\n");
  for(i=0;i<B;i++)
   {
    // printf("b %I64d\n",b[i]);
     for(j=0;j<m;j++)
      {
        if(b[i]==in[j].x)
         {
           a1[A]=in[j].x;
           a2[A]=in[j].p;
           A++;
         }
      }
     for(j=0;j<m;j++)
      {
        if(b[i]==in[j].y)
         {
           t=in[j].p;
           while(t>0)
            {
              A--;
              tt=a2[A];
            //  printf("bew %I64d %I64d   %d\n",t,tt,A);
              if(tt>=t)
               {
                 a2[A]-=t;
                 ff=cal(a1[A],b[i],t);
                 bb+=ff;
                 bb%=MOD;
                 A++;
                 break;
               }
              else
               {
                 ff=cal(a1[A],b[i],tt);
                 bb+=ff;
                 bb%=MOD;
                 t-=tt;
               }
            //  printf("1");
            }
         }
      }
   }
 // printf("%d %I64d %I64d\n",A,aa,bb);
  aa%=MOD;
  bb%=MOD;
  aa+=MOD;
  aa=aa-bb;
  if(aa<=0)aa+=MOD;
  if(aa<=0)aa+=MOD;
  aa%=MOD;
  printf("Case #%d: %d",ii,aa);
  if(ii<=T-1)printf("\n");
 }
    
    
    scanf(" ");
    return 0;
}
