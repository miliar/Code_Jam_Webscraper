#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    long long t;
    cin>>t;
    long long tc=1;
    while(t--)
    {
        int num;
        cin>>num;
        long long x=1;
        long long a[10];
        for(int i=0;i<10;i++)
        a[i]=0;
        long long rem;
        long long number=num;
        if(num==0)
        {
            cout<<"Case #"<<tc<<": INSOMNIA"<<endl;
        }
        else
        while(1)
        {
            long long y=num;
            while(num!=0)
            {
              rem=num%10;
              a[rem]=1;
              num=num/10;
            }
            int flag=1;
            for(int i=0;i<10;i++)
            {
                if(a[i]==0)
                {
                    flag=0;
                    break;
                }
                else
                {
                    flag=1;
                }
            }
            if(flag==1)
            {
                cout<<"Case #"<<tc<<": "<<y<<endl;
                break;
            }
            x++;
            num=number*x;
            //cout<<num<<endl;
        }
        tc++;
    }
}
