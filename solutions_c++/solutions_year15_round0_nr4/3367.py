#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int T,n;
int x,y;
int ans;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-smallout.txt","w",stdout);
    int i,j,k,ii;
    scanf("%d",&T);
for(ii=1;ii<=T;ii++)
{
  scanf("%d",&n);
  scanf("%d %d",&x,&y);
  ans=0;
  if(x>y)swap(x,y);
  if(x==1 && y==1)
   {
    if(n==1)ans=1;
   }
  else if(x==1 && y==2)
   {
    if(n==1 || n==2)ans=1;
   }
  else if(x==1 && y==3)
   {
    if(n==1)ans=1;
   }
  else if(x==1 && y==4)
   {
    if(n==1 || n==2)ans=1;
   }
  else if(x==2 && y==2)
   {
    if(n==1 || n==2)ans=1;
   }
  else if(x==2 && y==3)
   {
    if(n==1 || n==2 || n==3)ans=1;
   }
  else if(x==2 && y==4)
   {
    if(n==1 || n==2)ans=1;
   }
  else if(x==3 && y==3)
   {
    if(n==1 || n==3)ans=1;
   }
  else if(x==3 && y==4)
   {
    if(n==1 || n==2 || n==3 || n==4)ans=1;
   }
  else if(x==4 && y==4)
   {
    if(n==1 || n==2 || n==4)ans=1;
   }
  
  
  printf("Case #%d: ",ii);
  if(ans==0)printf("RICHARD\n");
  else printf("GABRIEL\n");
}

       
    
    
   // scanf(" ");
    return 0;
}
