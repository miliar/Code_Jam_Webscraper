#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;
int main()
{
    int t,n;
    FILE *fp,*op;
    fp=fopen("A-large.in","r");
    op=fopen("output.txt","w");
    int guest=0,cnt;
    char str[1002];
    fscanf(fp,"%d",&t);
    int p=1;
    while(t--)
    {
      fscanf(fp,"%d %s",&n,str);

      guest=0,cnt=0;
      for(int i=0;i<=n;i++)
      {
          if(cnt<i&&(str[i]-'0')>0)
          {
              guest+=i-cnt;
            cnt+=(i-cnt);
          }
          cnt+=(str[i]-'0');
      }

      fprintf(op,"Case #%d: %d\n",p,guest);
      p++;

    }


    fclose(fp);
    fclose(op);
}
