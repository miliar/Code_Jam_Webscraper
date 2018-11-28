#include <iostream>

using namespace std;

int main()
{
   int n,i,j,k,c,ans,p,ans2;
   float a[100],b[100],temp,a2[100],b2[100];
   cin>>n;
   if(n<=50&&n>=1)
  { for(i=0;i<n;i++)
   {   cin>>c;
       ans=0;
       ans2=0;
       
      if(!(c>=1&&c<=10))
       return 0;
       for(j=0;j<c;j++)
            {
                cin>>a[j];
            }
         for(j=0;j<c;j++)
            {
                cin>>b[j];
            }  
          
            
           for(j=0;j<c-1;j++)
           {   
              for(k=j+1;k<c;k++)
              {  if(a[j]<a[k])
                 {
                     temp= a[j];          
                        a[j] = a[k];
                        a[k] = temp;
                 }
              }
           }
           for(j=0;j<c-1;j++)
           {   
              for(k=j+1;k<c;k++)
              {  if(b[j]<b[k])
                 {
                     temp= b[j];          
                        b[j] = b[k];
                        b[k] = temp;
                 }
              }
           }
           
           for(j=0;j<c;j++)
            {
                a2[j]=a[j];
            } 
            for(j=0;j<c;j++)
            {
                b2[j]=b[j];
            }
            
            for(j=0;j<c;j++)
           {  if(b2[j]>0) 
             { for(k=0;k<c;k++)
              {  if(a2[k]>0)
                 { if(b2[j]>a2[k])
                 {  b2[j]=-1;
                    for(p=c-1;p>=0,a2[p]>0;p--)
                    {
                        a2[p]=-1;
                        break;
                    }
                    ans++;
                    break;
                     
                 }
                 if(b2[j]<a2[k])
                 {  b2[j]=-1;
                    a2[k]=-1;
                    
                    break;
                    
                     
                 }
              }}
           }}
           
           
          for(j=0;j<c;j++)
           {  if(a[j]>0) 
             { for(k=0;k<c;k++)
              {  if(b[k]>0)
                 { if(a[j]>b[k])
                 {  a[j]=-1;
                    for(p=c-1;p>=0,b[p]>0;p--)
                    {
                        b[p]=-1;
                        break;
                    }
                    ans2++;
                    break;
                     
                 }
                 if(a[j]<b[k])
                 {  a[j]=-1;
                    b[k]=-1;
                    
                    break;
                    
                     
                 }
              }}
           }}
          
        cout<<"Case #"<<i+1<<": "<<c-ans<<" "<<ans2<<"\n"; 
   }
  }
   return 0;
}
