#include<cstdio>
#include<cstring>
char s[2001];
int num[10];
int chk[2001];
int p[26];
int main()
{
    int t,n;
    scanf("%d",&t);
    for(int tcase=1;tcase<=t;tcase++)
    {
      scanf("%s",s);
      n=strlen(s);
      for(int i=0;i<10;i++) num[i]=0;
      for(int i=0;i<n;i++) chk[i]=0;
      for(int i=0;i<26;i++) p[i]=0;
      for(int i=0;i<n;i++)
      {
         if(s[i]=='Z')
          {
            num[0]++;
            chk[i]=1;
            p['E'-'A']++;
            p['R'-'A']++;
            p['O'-'A']++;
          }
         else if(s[i]=='W')
         {
           num[2]++;
           chk[i]=1;
           p['T'-'A']++;
           p['O'-'A']++;
         }
         else if(s[i]=='X')
         {
           num[6]++;
           chk[i]=1;
           p['S'-'A']++;
           p['I'-'A']++;
         }
         else if(s[i]=='U')
         {
           num[4]++;
           chk[i]=1;
           p['F'-'A']++;
           p['O'-'A']++;
           p['R'-'A']++;
         }
      }
      for(int i=0;i<n;i++)
      {
           if(chk[i]==0&&p[s[i]-'A']>0)
           {
             chk[i]=1; p[s[i]-'A']--;
           }
      }
      for(int i=0;i<n;i++)
      {
        if(chk[i]==0)
        {
          if(s[i]=='S')
          {
            num[7]++;
            chk[i]=1;
            p['E'-'A']+=2;
            p['N'-'A']++;
            p['V'-'A']++;
          }
          else if(s[i]=='F')
          {
            num[5]++;
            chk[i]=1;
            p['I'-'A']++;
            p['V'-'A']++;
            p['E'-'A']++;
          }
          else if(s[i]=='O')
          {
            num[1]++;
            chk[i]=1;
            p['N'-'A']++;
            p['E'-'A']++;
          }
        }
      }
      for(int i=0;i<n;i++)
      {
           if(chk[i]==0&&p[s[i]-'A']>0)
           {
             chk[i]=1; p[s[i]-'A']--;
           }
      }
      for(int i=0;i<n;i++)
      {
        if(chk[i]==0)
        {
          if(s[i]=='G')
          {
            num[8]++;
            chk[i]=1;
            p['I'-'A']++;
            p['H'-'A']++;
            p['E'-'A']++;
            p['T'-'A']++;
          }
          if(s[i]=='R')
          {
            num[3]++;
            chk[i]=1;
            p['T'-'A']++;
            p['H'-'A']++;
            p['E'-'A']+=2;
          }
        }
      }
      for(int i=0;i<n;i++)
      {
           if(chk[i]==0&&p[s[i]-'A']>0)
           {
             chk[i]=1; p[s[i]-'A']--;
           }
      }
      for(int i=0;i<n;i++)
      {
        if(chk[i]==0&&s[i]=='E')
        num[9]++;
      }
      printf("Case #%d: ",tcase);
      for(int i=0;i<10;i++)
      {
        for(int j=1;j<=num[i];j++)
          printf("%d",i);
      }
      printf("\n");
    }
    return 0;
}
