#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
    long T, numbers, no[10], prod, length=0, rdigit, prod1;

    cin>>T;
    long N[T];

    for (long lvar = 0; lvar<T; lvar++)
        cin>>N[lvar];

    for (long lvar1 = 0; lvar1<T; lvar1++)
    {

        for (int lvar2 = 0; lvar2<10; lvar2++)
            no[lvar2]=0;

        numbers = 0; length = 0;

        for (long lvar3 = 1; lvar3<=256000000; lvar3++)
        {
            prod = N[lvar1]*lvar3;
            prod1 = prod;
            length = 0;

            while (prod1 > 0)
            {
                ++length;
                prod1/=10;
            }

            prod1 = prod;


            for (int lvar4 = 0; lvar4<length; lvar4++)
            {
                    rdigit = prod1 % 10;

                    if (no[rdigit] == 0)
                        {
                            no[rdigit] = 1;
                            ++numbers;
                        }

                    prod1/=10;
            }

            if (numbers == 10)
                break;
        }

        if (numbers == 10)
        {
            cout<<"Case #"<<lvar1+1<<": "<<prod<<endl;;
        }

        else
            cout<<"Case #"<<lvar1+1<<": "<<"Insomnia"<<endl;

        prod=0; prod1=0;
    }

    getch();
    return 0;
}
