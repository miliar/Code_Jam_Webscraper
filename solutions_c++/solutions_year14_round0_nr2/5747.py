#include <iostream>

using namespace std;

int main()
{
   int n,i,q=1;
   float ans=0,d=2,c,f,x,temp=0;
   cin>>n;
   if(n<=100&&n>=1)
  { for(i=0;i<n;i++)
   {   cin>>c;
       cin>>f;
       cin>>x;
       q=1;
       d=2;
       ans=x/2;
       temp=0;
      if(!(c>=1&&c<=500&&f>=1&&f<=4&&x>=1&&x<=2000))
       return 0;
       while(q!=0)
           { 
            
            
           
            temp=temp+c/d;
            d=d+f;
            temp=temp+x/d;
            if(temp<=ans)
             {   ans=temp;
                 temp=temp-x/d;
             }
            
            if(temp>ans)
            {
               q=0; 
            }
           }
      
        cout<<"Case #"<<i+1<<": "<<ans<<"\n"; 
   }
  }
   return 0;
}
