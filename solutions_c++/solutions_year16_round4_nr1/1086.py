#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
int t,n;
int A[5];
int thislevel[5][20];
int ans;
int gg[5000];
int cnt;
int skips;
int fin;
bool solve(int a)
{
int total;
total=(1<<n);
thislevel[a][0]=1;
for(int i=1;i<=3;i++)
{
 if(i!=a)
 {
  thislevel[i][0]=0;
 }
}
//printf("%d %d %d\n",thislevel[1][0],thislevel[2][0],thislevel[3][0]);
 for(int i=1;i<=n;i++)
 {
  thislevel[1][i]=thislevel[1][i-1]+thislevel[3][i-1];
  thislevel[2][i]=thislevel[2][i-1]+thislevel[1][i-1];
  thislevel[3][i]=thislevel[3][i-1]+thislevel[2][i-1];
  //printf("%d %d %d\n",thislevel[1][i],thislevel[2][i],thislevel[3][i]);
 }
 /*printf(">> ");
 for(int i=1;i<=3;i++)
 {
  printf("%d ",thislevel[i][n]);
 }
 printf("\n");*/
 if(thislevel[1][n]==A[1]&&thislevel[2][n]==A[2]&&thislevel[3][n]==A[3]){return true;}
 return false;
}
void pri(int a,int depth)
{
  if(depth==n)
  {
   cnt++;
   if(a==1){gg[cnt]='R';}
   else if(a==2){gg[cnt]='S';}
   else{gg[cnt]='P';}
  }
  else if(a==0){printf("IMPOSSIBLE\n");}
  else if(a==1)
  {
   pri(1,depth+1);
   pri(2,depth+1);
  }
  else if(a==2)
  {
   pri(3,depth+1);
   pri(2,depth+1);   
  }
  else
  {
   pri(3,depth+1);
   pri(1,depth+1); 
  }
}
void expri()
{
// printf(">> ");
 for(int i=1;i<=cnt;i++)
 {
  printf("%c",gg[i]);
 }
 printf("\n");
}
int mycmp(int st1,int st2,int len)
{
char tmp;
 for(int i=0;i<len;i++)
 {
  if(gg[st1+i]<gg[st2+i]){return 0;}
  else if(gg[st2+i]<gg[st1+i])
  {
   for(int j=0;j<len;j++)
   {
    //printf("??? %c %c\n",gg[1],gg[3]);
    tmp=gg[st1+j];
    //printf("??? t %c st1 %c st2 %c\n",tmp,gg[st1+j],gg[st2+j]);
    gg[st1+j]=gg[st2+j];
   // printf("??? t %c st1 %c st2 %c\n",tmp,gg[st1+j],gg[st2+j]);
    gg[st2+j]=tmp;
   // printf("??? t %c st1 %c st2 %c\n",tmp,gg[st1+j],gg[st2+j]);
    //printf("sw %d %d",st1+j,st2+j);
   // expri();
   }

   return 0;
  }
 }
}

main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%d%d%d%d",&n,&A[1],&A[3],&A[2]);
  fin=1<<n;
  ans=0;
  cnt=0;
  for(int i=1;i<=3;i++)
  {
   if(solve(i)){ans=i;break;}
  }
  printf("Case #%d: ",tests);
 
  pri(ans,0);
  if(ans!=0)
  {
  for(int i=0;i<n;i++)
  {
   skips=(1<<i);
  // printf("ss %d\n",skips);
   for(int j=1;j<=fin;j=j+(2*skips))
   {
    mycmp(j,j+skips,skips);
    //printf("after %d %d %d :",j,j+skips,skips);
    //expri();
    }
  }
  expri();
  }
 }
 
 return 0;
}
