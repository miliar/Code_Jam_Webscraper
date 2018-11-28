#include<iostream>
using namespace std;
int main()
{
    int t,i,d;
    int arr[10],c,t1;
    long long n,n1;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        for(c=0;c<10;c++)
        arr[c]=0;

         c=0;
        if(n==0)
        {

            cout<<"Case #"<<i<<": INSOMNIA\n";
        }
        else
        {
            t1=1;
            while(c!=10)
            {

                n1=n*t1;
                while(n1!=0)
                {
                    d=n1%10;
                    n1/=10;
                    if(arr[d]!=1)
                    {
                        arr[d]=1;
                        c++;
                    }
                }
                t1++;
            }
            cout<<"Case #"<<i<<": "<<n*(t1-1)<<endl;
        }
    }
    return 0;
}
