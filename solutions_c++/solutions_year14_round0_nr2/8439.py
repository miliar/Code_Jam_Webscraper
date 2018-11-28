#include <iostream>

using namespace std;

int main()
{
    short T;
    cin>>T;
    cout.setf(ios_base::fixed, ios_base::floatfield);
    cout.precision(7);
    for(short i=0; i<T; i++)
    {
        long double C, F, X, U;
        U=0;
        cin>>C>>F>>X;
        unsigned long long j=0;
        while(true)
        {
            if(((X-C)/(2+j*F)-X/(2+(j+1)*F))>0)U+=C/(2+j*F);
            else
            {
                U+=X/(2+j*F);
                break;
            }
            j++;
        }
        cout<<"Case #"<<i+1<<": "<<U<<endl;
    }
    return 0;
}
