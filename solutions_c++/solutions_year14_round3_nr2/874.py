#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int cas=1;      
char a[100];
int n;
char b[100];
char tmp[120];
int ans;
int flag[120];
int seq[120];
int ap[120];
void print(int x)
{
  for(int i=0;i<26;i++)
  {
     cout<<x%2;
     x/=2;
  }
}
void dfs(int k,int now)
{
   if(k>=n)
   {
      ans++;
      /*for(int i=0;i<n;i++)
        printf("%d ",seq[i]);
      cout<<endl;*/
   }
   for(int i=0;i<n;i++)
   {
       if(flag[i]==0&&((now&ap[i])==0||(a[i]==b[seq[k-1]])&&((now&ap[i]^(1<<(a[i]-'a')))==0)))
          flag[i]=1,seq[k]=i;
       else
          continue;
       /*for(int j=0;j<=k;j++)
          cout<<"---";
       cout<<i<<' ';print(now);cout<<' ';print(ap[i]);cout<<endl;*/
       dfs(k+1,now|ap[i]);
       flag[i]=0;
   }
}
int check(int k)
{ 
   ap[k]=1<<(tmp[0]-'a');  
   for(int i=1;tmp[i];i++)
   {
      if(tmp[i]!=tmp[i-1])
      {
         if(ap[k]&(1<<(tmp[i]-'a')))
            return 1;
         ap[k]=ap[k]|(1<<(tmp[i]-'a'));
      }
   }
   return 0;
}        
int main()
{
    freopen("y3.in","r",stdin);
    freopen("y3.out","w",stdout);
    int t;
    cin>>t;
    while(t--)
    {
      cin>>n;
      ans=0;
      int w=0;
      memset(flag,0,sizeof(flag));
      memset(ap,0,sizeof(ap));
      for(int i=0;i<n;i++)
      {
         scanf("%s",tmp);
         a[i]=tmp[0];
         b[i]=tmp[strlen(tmp)-1];
         if(check(i))
            w=1;
      }
      if(w)
        ans=0;
      else
        dfs(0,0);
      printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
      
                
