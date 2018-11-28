#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int T,n;
char a[1011];
int now,ans;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-largeout.txt","w",stdout);
    int i,j,k,ii;
    scanf("%d",&T);
for(ii=1;ii<=T;ii++)
{
  scanf("%d",&n);
  scanf("%s",a);
  ans=0;now=0;
  for(i=0;i<=n;i++)
  {
    k=a[i]-'0';
   if(k != 0)
   {
    if(now < i)
     {
       ans += i - now;
       now = i + k;
     }
    else
     {
       now += k;
     }
    }
  }
  printf("Case #%d: %d\n",ii,ans);
}

    
    
    
   // scanf(" ");
    return 0;
}
