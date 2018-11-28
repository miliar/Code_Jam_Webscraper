#include<iostream>
#include<string.h>
#include<stdio.h>

using namespace std;

int main()
{
   int i,j,t,n,s,p,c;
   string a;

   cin>>t;
   
   int r[t];

   for(i=0;i<t;i++)
     {
         cin>>n;
         cin>>a;

         s=0;
         p=0;
         
         for(j=0;j<=n;j++)
          {
             switch(a[j])
                {
                      case '0' : c=0;break;
                      case '1' : c=1;break;
                      case '2' : c=2;break;
                      case '3' : c=3;break;
                      case '4' : c=4;break;
                      case '5' : c=5;break;
                      case '6' : c=6;break;
                      case '7' : c=7;break;
                      case '8' : c=8;break;
                      case '9' : c=9;break;
                 } 
           
             
             if(c!=0)
               {
                 if(j>s)
                   {
                       p=p+j-s;
                       s=j+c;
                   }
                  else s=s+c;
               }

              //if(n<=s)
              //break;
          }
        
          r[i]=p;
      }

      for(i=0;i<t;i++)
      {
        cout<<"case #"<<i+1<<": "<<r[i]<<endl;
      }
}

       
         
             
                    


    
