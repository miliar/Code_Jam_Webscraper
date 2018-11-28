#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int i,t,stand,borrow,sm,caseno;
    char man[1020];
    freopen("A-large.in","r",stdin);
    freopen("ou.out","w",stdout);
    cin>>t;
    for(caseno=1; caseno<=t; caseno++)
    {

        cin>>sm>>man;
        stand=0;
        borrow=0;
        for(i=0; i<=sm; i++)
        {
            if(stand>=i)
            {

                stand=stand+(man[i]-48);
            }
            else
            {
                borrow+=(i-stand);
                stand+=(i-stand);
                stand+=(man[i]-48);
            }
        }
       cout<<"Case #"<<caseno<<": "<<borrow<<endl;


    }
    return 0;

}

