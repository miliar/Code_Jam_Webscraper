#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
      long long n,k;
      cin>>n;
      k=n;
    int a[10];
    memset(a,0,sizeof(a));
    if(n==0)
        cout<<"Case #"<<i<<": "<<"INSOMNIA"<<"\n";
    else{
    while(1>0)
    {
        long long nn=n;
        while(nn>0)
        {
            int d=nn%10;
            a[d]=1;
            nn=nn/10;
        }
        int flag=0;
        for(int i=0;i<=9;i++)
        {
            if(a[i]==0)
                flag=1;
        }
        if(flag==0){
            cout<<"Case #"<<i<<": "<<n<<"\n";
            break;
        }
        else
            n+=k;
    }
    }
    }

}
