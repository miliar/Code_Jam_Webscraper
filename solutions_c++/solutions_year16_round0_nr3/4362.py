#include<bits/stdc++.h>
using namespace std;
//long long arr[1000005]={0};
long long power(long long a,long long b)
{
    if(b==0)
        return 1;
    else if(b%2==0)
            {
                long long s=power(a,b/2);
                return s*s;
            }
            else
                return a*power(a,b-1);
}
long long pri(long long p)
{
    for(int j=2;j<=sqrt(p);j++)
    {
        if(p%j==0)
        {
            return 1;
        }
    }
    return 0;
}
int main()
{

ios_base::sync_with_stdio(false);
	cin.tie(false);

//    sieve();
    long long t;
    cin>>t;
    long long count1=0;
    while(t--)
    {
        count1++;

long long n,jl;
cin>>n>>jl;
        cout<<"Case #"<<count1<<":\n";
long long ans=0;
long long sum[11];
for(long long i=(1<<(n-1));i<(1<<n);i++)
{
    if(i%2==0)
        continue;
  //  cout<<i<<endl;
    long long flag=0;
    if(ans>=jl)
        break;
        for(long long k=0;k<=10;k++)
            sum[k]=0;
            for(long long k=2;k<=10;k++)
        {

        for(long long j=0;j<n;j++)
    {
        if((i&(1<<j)))
           {
           // cout<<"fcgvhb"<<"\n";
               sum[k]+=(power(k,(j)));
           }
    }
    //cout<<sum[k]<<" ";
    if(pri(sum[k])==0)
    {
        flag=1;
        break;
    }

}
if(flag==0)
{
    ans++;
    cout<<sum[10]<<" ";
    for(long long p=2;p<=10;p++)
    {
        for(long long q=2;q<sum[p];q++)
        {
            if(sum[p]%q==0)

            {
        //  cout<<"p:"<<p<<" ";

                cout<<q<<" ";
            break;
        }
        }
    }
    cout<<"\n";
}
}
}
}
