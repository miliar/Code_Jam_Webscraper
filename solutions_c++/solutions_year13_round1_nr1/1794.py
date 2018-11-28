#include <iostream>
#include <algorithm>
using namespace std;

#define PI 3.1415926
long long r,t;


int calc()
{
    long long last_r = r;
    long count = 0;
    long long remain = t;
    long long total = 0;
    long n = 1;

    while(1)
    {            
        total += 2 *r + 4 * n - 3;
        
        if(total > remain)
            break;
        count++;
        n++;
    }

    return count;
}


int main()
{
   int test_case;
   cin>>test_case;

   for(int i = 0; i < test_case; ++i)
   {
        cin>>r>>t;
        cout<<"Case #"<<i+1<<": "<<calc()<<endl;
   }

    return 0;
}


