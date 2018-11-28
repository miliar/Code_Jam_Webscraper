#include <iostream>

using namespace std;

int main()
{
    long long int t,n,z,r,thick,i,c;
    cin>>t;
    
    for(z =1;z<=t;z++)
    {
          cin>>r>>thick;
          
          i = 0;
          c = (r+1)*(r+1) - r*r;
          //thick = thick -c;
          //i = 1 + (thick -c*r)/4;
          while(1)
          {
                  thick = thick - c- i*4;
                  if(thick<0)
                  break;
                  else if(thick==0)
                  {
                      i++;
                      break;
                  }
                  n +=2;
                  i++;
          } 
          cout<<"Case #"<<z<<": "<<i<<"\n";
    }
   // system("PAUSE");
    return 0;
}
