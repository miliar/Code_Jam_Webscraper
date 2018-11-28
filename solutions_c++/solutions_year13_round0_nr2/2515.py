#include<iostream>

using namespace std;

int main()
{
 int i,j,t,z,n,m;
 int ch,a[101][101],x[101],y[101];

 freopen("B-large.in", "r", stdin);
 freopen("output.txt", "w", stdout);
 
 scanf("%d",&t);
 
 for(z=0;z<t;z++)
 {
  scanf("%d%d",&n,&m);
  
  for(i=0;i<n;i++)
  for(j=0;j<m;j++)
  scanf("%d",&a[i][j]);
  
  for(i=0;i<n;i++)
  {
   ch=0;
   for(j=0;j<m;j++)
   if(ch<a[i][j])
   ch=a[i][j];                     
    
   x[i]=ch;
  }//i loop
  
  for(j=0;j<m;j++)
  {
   ch=0;
   for(i=0;i<n;i++)
   if(ch<a[i][j])
   ch=a[i][j];                     
    
   y[j]=ch;
  }//i loop
  
  ch=0;
  
  for(i=0;i<n;i++)
  {
   for(j=0;j<m;j++)
   if((a[i][j]!=x[i])&&(a[i][j]!=y[j]))                
   { ch=1; break;}
   
   if(ch==1)
   break;
  }   
  
  if(ch==1)
  printf("Case #%d: NO\n",z+1);
  
  else
  printf("Case #%d: YES\n",z+1);
 }
 
 cin>>i;   
 return 0;   
}
