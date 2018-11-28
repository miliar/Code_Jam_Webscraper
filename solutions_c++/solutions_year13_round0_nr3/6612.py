#include<iostream>
#include<math.h>

using namespace std;

int pal(int args)              
{
	int co,l;
	co=0;
   	int x = args;
    while(args)
    {
	       l=(co*10);
               co = l + ( args % 10 );
               args /= 10;
    }
    if(co == x)
    	return 1;
    
    else 
    	return 0;
}


int main()
{
    int timepass1,temp;
    int c=0,j,a,b,success=0;

    j=1;

    cin>>timepass1;
    
    while(timepass1--)
    {
              success = 0;
              cin>>a;
              cin>>b;
              a--;
              while((a)!=(b))
              {
                         a++;
                         c=sqrt(a);

                         if( (c*c) != a)

                         continue;
                         
                         if(pal(a) && pal(c))
                         {
                            success++;
                         }
                                          
               }

         cout<<"Case #"<<j<<": "<<success<<"\n";
         j++;
      }
              
          cin>>temp;
}
