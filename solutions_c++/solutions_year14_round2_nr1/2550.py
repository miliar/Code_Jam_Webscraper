#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define MAX 110
char a[MAX][110];
char b[MAX][110];
int cntC[MAX][110];
int cnt[MAX];
int n;

int doit()
{

    memset(cntC,0,sizeof(cntC));
  for(int j=0;j<n;j++)
  {
    b[j][0]=a[j][0];
    cnt[j]=0;
    cntC[j][0]=1;
    for(int i=1;i<strlen(a[j]);i++)
    {
      if(a[j][i]==a[j][i-1])
      {
        cntC[j][cnt[j]]++;
      }
      else
      {
        cntC[j][++cnt[j]]=1;
        b[j][cnt[j]]=a[j][i];
      }
    }
    b[j][++cnt[j]]='\0';
  }
  int res=0;
  for(int i=0;i<n;i++)
  {
    if(cnt[i]!=cnt[0])
      return -1;
    for(int j=0;j<cnt[0];j++)
      if(b[i][j]!=b[0][j])
        return -1;
  }
  for(int j=0;j<n;j++)
  {
    for(int i=0;i<cnt[0];i++)
    {
    //  printf("cntC[%d][%d]=%d\n",j,i,cntC[j][i]);
      res+=cntC[j][i]-1;
    }
  }
  for(int k=0;k<n;k++)
  {
    int tmp=0;
    for(int j=0;j<n;j++)
    {
      for(int i=0;i<cnt[0];i++)
      {
      //  printf("cntC[%d][%d]=%d\n",j,i,cntC[j][i]);
        tmp+=abs(cntC[j][i]-cntC[k][i]);
      }
    }
    if(tmp<res)
      res=tmp;
  }
  return res;
}

int main()
{
  int T;
  int ca=0;
  scanf("%d",&T);
  while(T--)
  {
    scanf("%d",&n);
    for(int i=0;i<n;i++)
      scanf("%s",a[i]);
    int res = doit();
    printf("Case #%d: ",++ca);
    if(res==-1)
      printf("Fegla Won\n");
    else
      printf("%d\n",res);

  }
}
