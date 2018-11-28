#include<cstdio>
#include<cstring>
using namespace std;
char str[105];
int n;
bool isV(char x)
{
   if(x=='a'||x=='e'||x=='i'||x=='o'||x=='u') return true;
   return false;
}
bool check(int st,int end)
{
   int i,j,s,e;
   for(i=st; i<=end; i++)
   {
      if(isV(str[i])) continue;
      s=i;
      while(!isV(str[i]) && i<=end) i++;
      e=i;
      if(e-s>=n) return true;
      i--;       
   }  
   return false;
}
int main()
{
    int T,l,i,j,c=0,l1,Ans;
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
       scanf("%s%d",str,&n);
       l=strlen(str);
       Ans=0;
       for(i=0; i<l; i++)
       {
          for(j=0; j<l; j++)
          {
             l1=j-i+1;
             if(l1<n) continue;
             if(check(i,j)) Ans++;      
          }      
       }
       printf("Case #%d: %d\n",++c,Ans);       
    }
    return 0;
}
