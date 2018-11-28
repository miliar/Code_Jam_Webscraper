#include<iostream>
#include<stdio.h>
#include<algorithm>
#define rep(i,a,b) for(i=a;i<=b;i++)
using namespace std;


/*double solve(double c,double x,double initial,double rate, int time)
{
       double ans, t1, t2,t3;
       
       t1=(x/initial) + time ;
       t2=(x/(initial+rate)) + c/(initial) +time ;
       
       
       if(t1<=t2)
       return t1;
       
       
       else 
       {
            t2= c /initial + solve(c,x,initial+rate, rate , time + c/initial);
            
            return t2;
       }
       
       
       
       
}*/


int main()
{   freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int t,m;
    
    double c,f,x,waste,current,advance,t1,t2;
    cin>>t;
    rep(m,1,t)
    {
      cin>>c>>f>>x;
      //ans=solve(c,x,2.0,f,0.0);
      waste = 0;
      current=2.0;
      advance=2.0 + f;
      t1=x/current + waste;
      waste+= c/current;
      t2=x/advance + waste ;
      while(t1>t2)
      {   
          t1=t2;
          waste+= c/advance;
          current = advance;
          advance+=f;
          t2 = waste + x/advance;
                  
      }
      
      
      
     printf("Case #%d: %.7lf\n",m,t1);
      
    }
    
    return 0;
}
