#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t, T;
    double c, f, x, divfactor, tott, curt, prevt, cfactor, xfactor;
    cin>>T;
    for(t = 0; t < T; t++)
    {
          tott = curt = 0;
          divfactor = 2.0;
          cin>>c>>f>>x;
          prevt = x / divfactor;
          
          while(1)
          {
    
                cfactor = c / divfactor;
                divfactor += f; 
                xfactor = x /divfactor;
                curt = cfactor + xfactor;             
                if(prevt > curt)
                {
                        tott += cfactor;
                        prevt = xfactor;
                }
                else
                {
                        tott += prevt;
                        break;
                }
          }
          printf("Case #%d: %.7f",(t+1),tott);
//          cout<<"Case #"<<t+1<<": "<<tott;
          if(t < T-1)
               cout<<endl;
    }
    return 0;
}
