#include <iostream>
#include <math.h> 
#include <stdint.h>
using namespace std; 

int main()
{
    int numTest;
    cin>>numTest;
    for(int p=0;p<numTest;++p)
    {
        uint64_t r=0;
        uint64_t t=0;
        cin>>r;
        cin>>t;
        unsigned int  num = (( sqrt(16*r*r-16*r+32*t+4) - 4*r - 6) / 8 + 1);
        //int num = 1 + (-4*r-6+)/8;
        cout<<"Case #"<<p+1<<": "<<num<<endl;
    }
}
