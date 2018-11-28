#include <iostream>

using namespace std;

int main()
{
   int a[10]={0};
   int n,n1,n2,r=0,d=0,f=1,t,in[100];
   cin>>t;
   for(int q=0;q<t;q++)
   {
       cin>>in[q];
       
   }
   
   
   int k=0;
 
   //cin>>n;    //N
   while(k<t)
   {
      int a[10]={0};
       n=in[k];
   f=1,d=0,r=0;
   for(int i=1;d<10&&n!=0;i++)
   {
       n1=n*i;
       n2=n1;
       //cout<<"--"<<n2;
       while(n1>0)
       {
         r=n1%10;
         n1=n1/10;
         
         if(a[r]==0)
          {
            a[r]=1;
            d++;
          }
         
          f=0;
         /* for(int j=1;j<10;j++)
           {  
              if(a[j]==0)
               f=1;
           }*/
           
           if(d==10)
           {
             break;
           }
           
       }
       
        if(d==10)
           {
             break;
           }
       
   }
 
   
   
   k++;
   
 
   if(d==10)
   cout<<"Case #"<<k<<": "<<n2<<'\n';
   else
   cout<<"Case #"<<k<<": INSOMNIA\n";
   
   
       
   }
   return 0;
   
}



