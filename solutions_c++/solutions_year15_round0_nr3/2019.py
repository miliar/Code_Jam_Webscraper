#include <stdio.h>
#include <stdlib.h>

int fr[10001];
int la[10001];
int len;
int mul;
int lenmul;
int A[5][5];
char B[10001];
int tmp;
int t;
int ans;
int tmp2;
int solve()
{
 for(int i=0;i<lenmul-2;i++)
  {
   if(fr[i]==2)
   {
    //printf("i = %d %d\n",i,fr[i]);
    tmp=1;
    for(int j=i+1;j<lenmul-1;j++)
    {
     if(tmp<0){tmp2=-A[-tmp][B[j]];}
     else{tmp2=A[tmp][B[j]];}
     tmp=tmp2;
     if(tmp==3)
     {
      //printf("j = %d\n",j);
      if(la[j+1]==4){/*printf("!!!\n");*/return 1;}
     }
    }
   }
  }
  return 0;
}
main()
{
 freopen("C-small-attempt2.in","r",stdin);
 freopen("C-small-attempt2.out","w",stdout);
 A[1][1]=1;A[1][2]=2;A[1][3]=3;A[1][4]=4;
 A[2][1]=2;A[2][2]=-1;A[2][3]=4;A[2][4]=-3;
 A[3][1]=3;A[3][2]=-4;A[3][3]=-1;A[3][4]=2;
 A[4][1]=4;A[4][2]=3;A[4][3]=-2;A[4][4]=-1;
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%d%d",&len,&mul);
  scanf("%s",B);
  ans=0;
  for(int i=0;i<len;i++)
  {
   B[i]=B[i]-'i'+2;
  }
  for(int i=1;i<mul;i++)
  {
   for(int j=0;j<len;j++)
   {
   B[(i*len)+j]=B[j];
   }
  }
  lenmul=len*mul;
  fr[0]=B[0];
  //printf("|%d|,",B[0]);
  for(int i=1;i<lenmul;i++)
  {
   if(fr[i-1]<0){fr[i]=-A[-fr[i-1]][B[i]];}
   else{fr[i]=A[fr[i-1]][B[i]];}
   //printf("%d,",fr[i]);
  }
  //printf("\n");
  la[lenmul-1]=B[lenmul-1];
  la[lenmul]=0;
    for(int i=lenmul-2;i>=0;i--)
  {
   if(la[i+1]<0){la[i]=-A[B[i]][-la[i+1]];}
   else{la[i]=A[B[i]][la[i+1]];}
  }
  ans=solve();
  printf("Case #%d: ",tests);
  if(ans==1){printf("YES\n");}
  else{printf("NO\n");}
 }
 return 0;
}
