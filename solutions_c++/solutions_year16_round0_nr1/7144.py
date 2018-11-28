
#include <iostream>
#include <stdlib.h>

using namespace std;
int fallSleep(int);

int main()
{

    int T;
    int i;
    std::cin>>T;

    int N[T];

    for(i=0; i<T; i++)
    {
        std::cin>>N[i];
    }

    for(i=0; i<T; i++)
    {
        if(fallSleep(N[i]) == 0 )
            std::cout<<"Case #"<<i+1<<": INSOMNIA\n";
        else
            std::cout<<"Case #"<<i+1<<": "<<fallSleep(N[i])<<endl;
    }

    return 0;
}

int fallSleep(int n)
{

    int digit[10];
    int i,j,rem;

    int count=0;

    for(i=0; i<10; i++)
     digit[i]=-1;

    if(n == 0)
        return 0;

    for(i=1; count<10; i++)
    {
        j=n*i;
        for(; j>0; )
        {
            rem = j % 10;
            j -= rem;
            j = j/10;

            if(digit[rem] == -1)
            {
               digit[rem] = rem;
               count++;
               if(count == 10)
                    return n*i;

            }
        }

    }

}

