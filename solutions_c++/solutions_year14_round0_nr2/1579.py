#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
    int cases;
    double c, f, x;
    cin>>cases;
    
    for(int i=0; i<cases; ++i)
    {
        cin >>c>>f>>x;
        
        if(c > x)
        {
            printf ("Case #%d: %0.7lf\n", i+1, x/2);
        }
        
        else
        {
            int numF = x/c;
            double fastest=0.0;
            bool set = false;
            
            for(int j=0; j <= numF; ++j)
            {
                double seconds = 0.0;
                int farms = 0;
                for(int k=0; k<j; ++k)
                {
                    seconds += (c/(2+f*farms));
                    farms++;
                }
                seconds+= (x/(2+f*farms));
                if(!set)
                {
                    fastest = seconds;
                    set = true;
                }
                else if(fastest > seconds)
                    fastest = seconds;
            }
            
            printf("Case #%d: %0.7lf\n", i+1, fastest);

        }
    }
    
}