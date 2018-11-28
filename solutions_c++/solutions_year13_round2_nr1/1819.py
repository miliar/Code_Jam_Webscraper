#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>

using namespace std;

int main()
{
 int t,z,i,n,c,a,j,b;
  
 freopen("A-large.in", "r", stdin);
 freopen("output.txt", "w", stdout);
 
 scanf("%d",&t);
 
 for(z=0;z<t;z++)
 {
  scanf("%d%d",&a,&n);
  vector<int>num;
  
  for(i=0;i<n;i++)
  {
   scanf("%d",&c);
   num.push_back(c);                
  }
  
  sort(num.begin(), num.end());
  
  if(a==1)
  {
   printf("Case #%d: %d\n",z+1,n);
   continue;        
  }
  
  j=0; c=101;
  for(i=0;i<n;i++)
  {
   if(a>num[i])
   {
    a=a+num[i];
    continue;
   }
   
   else
   {
    //if(num[i]-a>=a)
    //{
     if(c>j+n-i)
     c=j+n-i; 
     
     //printf("%d\t%d\t%d\n",c,j,a);      
    //}
    
    a=(2*a)-1;
    i--;
    j++;           
   }//outer else
  }//for loop
  
  if(c<j)
  j=c;
    
  printf("Case #%d: %d\n",z+1,j);
 }
 
 cin>>i;   
 return 0;   
}
