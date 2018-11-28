#include <iostream>
#include <fstream>

using namespace std;

bool digits[10];

bool checkdigits()
{
    return (digits[0] && digits[1] && digits[2] && digits[3] && digits[4] && digits[5] && digits[6] && digits[7] && digits[8] && digits[9] );
}

main()
{
    ifstream in;

    in.open("A-large.in");
    int t;
    in>>t;

    for(int i=0;i<t;i++)
    {
        int n;
        in>>n;
        for(int j=0;j<10;j++)
            digits[j]=false;

        int sn=n;
        int k=1;
        while(!checkdigits())
        {
            if(sn==0)
                break;

            n=k*sn;

            while(n!=0)
            {
                int d=n%10;
                n/=10;
                digits[d]=true;

            }

            k+=1;
        }

        if(sn==0)
            cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<(k-1)*sn<<endl;
    }




}
