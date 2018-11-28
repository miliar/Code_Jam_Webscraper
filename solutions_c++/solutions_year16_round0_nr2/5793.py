#include<stdio.h>
#include<string.h>

using namespace std;
int main()
{

  int t,p,ans,n;
  char all[101];
  FILE * fin, * fot;
  fin = fopen ("largeB.in","r");
  fot = fopen ("ans.out","w");
  fscanf(fin,"%d",&t);

for(int i=0;i<t;i++)
{
  fscanf(fin,"%s",&all);
  ans=0;n=strlen(all);
  //printf("string:%s\n",all);
  int j=0;
  while(j+1<n&&all[j+1]==all[j])j++;
  if(all[j++]=='-')
    ans++;
  for(;j<n;j++)
  {
      while(j+1<n&&all[j+1]==all[j])j++;
      if(all[j]=='-')
        {
                ans+=2;
        }
    //printf("j:%d ans:%d\n",j,ans);
  }
  fprintf(fot,"Case #%d: %lld\n",i+1,ans);
}

  fclose(fin);
  fclose(fot);

}
