#include<bits/stdc++.h>
using namespace std;
int main()
{
    FILE *fr=fopen("A-large.in","r");
    FILE *fw=fopen("Output.txt","w");
    char str[100005];
    int tc,n,i;
    fscanf(fr,"%d",&tc);
    int ctr=1;
    while(tc--)
    {
      fscanf(fr,"%d%s",&n,str);
      int ans=0,stand=0;
      for(i=0;i<=n;i++)
      {
              if(stand<i)
              {
                ans+=(i-stand);
                stand=i;
              }
              stand+=str[i]-'0';

      }
      fprintf(fw,"Case #%d: %d\n",ctr++,ans);
    }
    return 0;
}
