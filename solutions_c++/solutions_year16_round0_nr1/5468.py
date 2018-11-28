#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output_large.txt","w",stdout);
    int t;
    cin>>t;
    int cnt=1,f1=0;
    while(t--)
    {
        long long n,b;
        cin>>n;
        int a[10]={0};
        for(long long i=1;i<=1000000;i++)
        {
            int flag=0;
            b=n*i;
            long long x=b;
            while(x)
            {
                a[x%10]=1;
                x/=10;
            }
            for(int i=0;i<10;i++)
            {
                if(a[i]==0)
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                f1=1;
                break;
            }
        }
        if(f1==1)
        cout<<"Case #"<<cnt<<": "<<b<<endl;
        else
        cout<<"Case #"<<cnt<<": INSOMNIA"<<endl;
        cnt++;
    }
}
