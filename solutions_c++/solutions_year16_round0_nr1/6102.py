#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    long long int t;
    cin>>t;
    long long int n;
    for(n=1;n<=t;n++)
    {
        long long int num[10];
        long long int i;
        for(i=0;i<=9;i++)
        {
            num[i]=1;
        }
        long long int flag=0;
        long long int x=0;
        long long int counter=1;
        long long int N;
        cin>>N;
        if(N!=0)
            flag=1;
        long long int temp;
        long long int res=0;
        while(true&&flag)
        {
            temp=N*counter;
            res=temp;
            while(temp!=0)
            {
                long long int xx=temp%10;
                temp=temp/10;
                if(num[xx]==1)
                {
                    x++;
                    num[xx]=0;
                }
            }
            counter++;
            if(x==10)
                break;
        }
        if(!flag)
            cout<<"Case #"<<n<<": "<<"INSOMNIA"<<endl;
        else
        {
            cout<<"Case #"<<n<<": "<<res<<endl;
        }
    }
    return 0;
}
