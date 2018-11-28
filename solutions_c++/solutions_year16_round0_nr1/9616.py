#include<bits/stdc++.h>
using namespace std;
int a[10];
int main()
{
    int t;
    scanf("%d",&t);

    for(int j=0;j<t;j++)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<10;i++)
        {
            a[i]=0;
        }
        if(n==0)
        {
            cout<<"Case #"<<j+1<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        int sum=n;
        int max_sum=101*n;
        int flag=1;
        while(sum<=max_sum)
        {
            int temp=sum;
            //cout<<sum<<endl;
            while(temp>0)
            {
                int x=temp%10;
                a[x]=1;

                temp/=10;
            }
            flag=1;
            for(int k=0;k<10;k++)
            {
                if(a[k]==0)
                {
                    flag=0;
                    break;
                }
            }
            if(flag==1)
            {
                cout<<"Case #"<<j+1<<": "<<sum<<endl;
                break;
            }
            sum+=n;
        }
        if(flag==0)
        {
            cout<<"Case #"<<j+1<<": "<<"INSOMNIA"<<endl;
        }
    }
    return 0;
}
