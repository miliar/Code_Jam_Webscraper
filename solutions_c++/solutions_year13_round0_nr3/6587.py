#include<iostream>
#include<math.h>
#include<sstream>
using namespace std;
int palin(double);

   int t,kp,z,d,l,m,n,i,j,val,val2,sum=0;
   double a,b;string ptr;
   int main()
{
   cin>>t;
   
   
   for(kp=1;kp<=t;kp++)
   {
       z=1;
       cin>>a>>b;
       for(;a<=b;a++)
       {
          double c=sqrt(a);
          d=int(c);
          if(d==c)
          {val=palin(a);}
          if(val==1){val2=palin(c);}
          if(val2==1)sum++;
          
        
        }    
          cout<<"Case #"<<kp<<": "<<sum<<endl; sum=0;          
   } 
           //system("PAUSE");
           return 0;
   }        
       
       
       int palin(double a)
       {
       stringstream ss;
                    ss<<a;
                     ptr=ss.str();l=ptr.length();
          if(l%2!=0)
          {m=l/2 -1;n=l/2 +1;}
          else
          {m=l/2 -1;n=l/2;}
          z=1;
          
          for(i=m,j=n;i>=0;i--,j++)
          if(ptr[i]==ptr[j])z=z*1;else z=0;
          return z;
      }    
