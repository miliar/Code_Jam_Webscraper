#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long t,x=0,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<++x<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        long long temp,t1=n;
        long long c=1;
        int hash[10]={0};
        while(1)
        {
            temp=t1;
            while(temp>0)
            {
                hash[temp%10]=1;
                temp/=10;
            }
            int flag=0;
            for(int i=0;i<10;i++)
            {
                if(hash[i]==1)
                {
                    flag+=1;
                }
            }
            if(flag==10)break;
            c+=1;
            //cout<<c<<endl;
            t1=n*c;
        }
        cout<<"Case #"<<++x<<": "<<t1<<endl;
    }

}
