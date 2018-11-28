#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#define N 105
using namespace std;
int n;
char s1[105],s2[105];
char s[105];
int num1[N],num2[N];
int main()
{
   // freopen("in.txt","r",stdin);
  // freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int test=1;
    while(T--)
    {
        memset(num1,0,sizeof(num1));
        memset(num2,0,sizeof(num2));
             scanf("%d",&n);
               scanf("%s",s1);
               scanf("%s",s2);
               int p=0;
               int len1=strlen(s1);
               int len2=strlen(s2);
              s[p]=s1[0];
              num1[0]++;
              for(int i=1;i<len1;i++)
              {
                  if(s1[i]!=s1[i-1])
                  {
                      p++;
                      s[p]=s1[i];
                  }
                  num1[p]++;
              }
              bool flg=true;
              num2[0]=1;
              int p2=0;
              if(s2[0]!=s[0])flg=false;
              for(int i=1;i<len2;i++)
              {
                  if(s2[i]!=s2[i-1])
                  {
                      p2++;
                      if(p2>p||s[p2]!=s2[i])
                      {
                          flg=false;
                          break;
                      }
                  }
                  num2[p2]++;
              }
              if(p!=p2)flg=false;
              if(!flg)
              {
                   printf("Case #%d: Fegla Won\n",test++);
                   continue;
              }
              int ans=0;
              for(int i=0;i<=p;i++)
                ans+=abs(num1[i]-num2[i]);
             printf("Case #%d: %d\n",test++,ans);
    }
}
