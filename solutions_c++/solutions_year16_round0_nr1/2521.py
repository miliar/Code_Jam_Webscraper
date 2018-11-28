#include <string>
#include <map>
#include <sstream>
#include<vector>
#include<iostream>
using namespace std;

int func(long long n,vector<int> &v)
{
    if(n==0)
    {
        return 1;
    }

    while(n!=0)
    {
        v[n%10]=1;
        n=n/10;
    }

    int c=1;

    for(int i=0; i<10; i++)
    {
        if(v[i]==0)
        {
            c=0;
            break;
        }
    }


    return c;

}

int main()
{

    vector<int> v(10);
    int t,ti;
    cin>>t;

    ti=t;
    for(; t>0; t--)
    {
        int i=0;
        for(i=0; i<10; i++)
        {
            v[i]=0;
        }

        long long n,no;

        cin>>n;
        no=n;

        while(true)
        {
            if(func(n,v)==1)
            {
                break;
            }
            n=n+no;
        }
        if(n==0)
        {
            cout<<"Case #"<<(ti-t+1)<<": INSOMNIA"<<endl;
        }
        else
        {
            cout<<"Case #"<<(ti-t+1)<<": "<<n<<endl;
        }
    }



    return 0;
}
