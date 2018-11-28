#include<iostream>
using namespace std;
int main()
{
    long t;
    cin>>t;
    for(long i=1;i<=t;i++)
    {
        long long n,m=0,m1=0;
        cin>>n;
        int a[10]={0};
        int c=0;
        if(n==0)
        cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
        {
            while(1)
            {
                m=m1+n;
                m1=m;
                int tmp;
                while(m>0)
                {
                    tmp=m%10;
                    if(a[tmp]==0)
                    {
                        a[tmp]=1;
                        c++;
                    }
                    m=m/10;
                }
                if(c==10)
                {
                    cout<<"Case #"<<i<<": "<<m1<<endl;
                    break;
                }
            }
        }
    }
    return 0;
}