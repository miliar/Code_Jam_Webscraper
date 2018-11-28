#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    long int n;
    int a[10];
    for(int k=1;k<=t;k++)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<k<<": "<<"INSOMNIA\n";
            continue;
        }
        for(int i=0;i<10;i++)
            a[i]=0;
        long int j=1,flag=1;
        long long int last,ans,temp,count=0;;
        while(flag)
        {
            ans=n*j;
            j++;
            last=ans;
            while(ans)
            {
               temp=ans%10;
               a[temp]++;
               if(a[temp]==1)
                    count++;
               ans=ans/10;
               if(count==10)
               {
                   flag=0;
                   break;
               }
            }
        }
        cout<<"Case #"<<k<<": "<<last<<"\n";
    }
    return 0;
}
