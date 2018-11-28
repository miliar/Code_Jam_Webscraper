#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    short unsigned int T = 0,c = 1;
    double C,F,X,last,current,BR = 2.0;
    unsigned int i = 0 , j = 0;
    cin>>T;
    while(T--)
    {
        cin>>C>>F>>X;
        last = X;
        for(i = 0;true;i++)
        {
            current = 0.0;
            current += (X / (BR + i*F));
            for(j = 1;j<=i;j++)
            {
                current += (C/(BR + (j-1)*F));
            }
            if(current > last)
                break;
            else
                last = current;
        }
        cout<<"Case #"<<c<<": ";
        std::cout << std::setprecision(6) << std::fixed;
        cout<<last<<endl;
        c = c + 1;
    }
}
