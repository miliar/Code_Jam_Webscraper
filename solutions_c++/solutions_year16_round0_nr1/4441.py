#include<iostream>
#include<stdio.h>
#include<cmath>
#include <bitset>
using namespace std ;

int main()
{
    int T,N;
    freopen("A-large.in","r",stdin) ;
    freopen("aout.txt","w",stdout) ;
    std::bitset<10> x;
    cin>>T;
    for (int i=1;i<=T;i++)
    {
        cin>>N;
        int m,d;
        x.reset();
        if (N==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
        else
        {
            int j=1;
            while (1)
            {
                m = N*j;
                while(m>0)
                {
                    d = m%10;
                    if (x[d]!=1)
                        x[d]=1;
                    m = m/10;
                }
                if (x.count()==10)
                {
                    m = N*j;
                    break;
                }
                j++;
            }
            cout<<"Case #"<<i<<": "<<m<<endl;
        }
    }
}
