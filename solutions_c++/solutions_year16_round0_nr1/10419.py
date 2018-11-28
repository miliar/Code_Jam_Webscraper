#include <iostream>
using namespace std;

int main()
{
    int t,d;
    long n,i=1,k,j;
    long long x,m;
    cin>>t;
    while(t>0)
    {
        cin>>n;
        if(n==0)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
        {
            d=0;k=1;
            int a[10]={0};
            while(d<10 && k<=100)
            {
                m = x = k * n;
                while(x!=0)
                {
                    j = x%10;
                    if(a[j]==0)
                    {
                        a[j]=1;
                        d++;
                    }
                    x/=10;
                }
                k++;
            }
            if(d==10)
                cout<<"Case #"<<i<<": "<<m<<endl;
            else
                cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
        t--;
        i++;
    }
}
