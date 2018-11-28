#include<iostream>
#include<fstream>
using namespace std;
int data[1401000];
long long int isprime(long long int t)
{
    int i;
    for(i=0;(data[i]*data[i])<t;i++)
    {
        if(i>1400490)
        {
            return -1;
        }
        if((t%data[i])==0)
        {
            return data[i];
        }
    }
    return -1;
}
int main()
{
    ifstream asd("prime");
    long long int i,j,k,l,b[11],t,ans[11],anscount;
    int a[16],allisprime;

    cout<<"Case #1:\n";
    data[0]=2;
    for(i=1;i<1400500;i++)
    {
        asd>>data[i];
    }

    for(i=1;i<=14;i++)
    {
        a[i]=0;
    }
    a[0]=1;a[15]=1;
    anscount =0;
    while(1)
    {
        for(i=0;i<=10;i++)
        {
            b[i]=0;
        }
        allisprime =1;
        for(i=2;i<=10;i++)
        {
            t=1;
            for(j=0;j<16;j++)
            {
                if(a[j])
                {
                    b[i]+=t;
                }

                t*=i;
            }
            k= isprime(b[i]);
            if(k==-1)
            {
                allisprime =0;
            }
            ans[i]=k;
        }
        if(allisprime)
        {
            anscount++;
            for(i=15;i>=0;i--)
            {
                cout<<a[i];
            }
            cout<<" ";

            for(i=2;i<=10;i++)
            {
                cout<<ans[i]<<" ";
            }
            cout<<endl;

        }
        if(anscount>50)
            break;

        a[1]++;
        for(i=1;i<14;i++)
        {
            if(a[i]==2)
            {
                a[i+1]++;
                a[i]=0;
            }
        }
        if(a[14]==2)
            break;
    }
}
