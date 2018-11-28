#include<iostream>
using namespace std;
int main()
{
    int t,n,ar[10],rem,m,test,times,currentm;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        for(int j=0;j<=9;j++)
        {
            ar[j]=0;
        }
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        }
        else
        {
            currentm=n;
            m=n;
            times=2;
            rev:
            test=0;
            while(m!=0)
            {
                rem=m%10;
                ar[rem]++;
                m=m/10;
            }
            for(int k=0;k<=9;k++)
            {
                if(ar[k]==0)
                {
                    m=n*times;
                    times++;
                    currentm=m;
                    goto rev;
                }
            }
            cout<<"Case #"<<i<<": "<<currentm<<endl;
        }
    }
    return 0;
}
