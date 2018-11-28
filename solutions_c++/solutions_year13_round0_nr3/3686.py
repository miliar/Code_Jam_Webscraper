#include <iostream>
#include <math.h>
using namespace std;

bool palindrome(uint64_t a)
{
    unsigned short* digits= new unsigned short[101];
    int i=0;
    while(a!=0)
    {
        digits[i]=a%10;
        a=a/10;
        ++i;
    }

    int length = i;
    
    for(int k=0;k<=length/2;++k)
    {
        if(digits[k]!=digits[length-1-k])
        {
            return false;
        }
    }

    delete [] digits;
    return true;
}

int main()
{
    int numTest;
    cin>>numTest;

    for(int k=0;k<numTest;++k)
    {
        uint64_t A,B;
        cin>>A>>B;

        uint64_t min=sqrt(A);
        if(min*min<A)
            min=min+1;
        uint64_t max=sqrt(B);
    
        int number = 0;

        for(uint64_t i=min; i<=max; ++i)
        {
            if(palindrome(i) && palindrome(i*i))
            {
                number++;
            }
        }
        
        cout<<"Case #"<<k+1<<": "<<number<<endl;
    }
    
    return 0;
}
