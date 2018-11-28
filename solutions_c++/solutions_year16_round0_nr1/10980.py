#include<bits/stdc++.h>
using namespace std;


int main()
{
    long long t,n,rem,mark[10],i,k,test,temp,flag;
    cin>>test;
    for(t=1;t<=test;t++)
    {
        cin>>n;
        if(n==0)
               cout<<"Case #"<<t<<": INSOMNIA"<<endl;
        else
        {
             for(i=0;i<10;i++)
            mark[i]=0;
        k=1;
        while(1)
        {
            temp=n*k;
            k++;
            while(temp>0)
            {
                rem=temp%10;
                mark[rem]=1;
                temp=temp/10;
            }
            flag=0;
            for(i=0;i<10;i++)
            {
                if(mark[i]==0)
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
                break;

        }
        cout<<"Case #"<<t<<": "<<n*(k-1)<<endl;
        }

    }
    return 0;
}
