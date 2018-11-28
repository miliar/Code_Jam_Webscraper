#include<bits/stdc++.h>

using namespace std;

long long power(long long base,long long p)
{
    if(p==0)
        return 1;
    if(p&1)
        return base*power(base,p-1);
    else
    {
        long long k=power(base,p/2);
        return k*k;
    }
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int k,c,s,t,num=1;
    cin>>t;
    while(t--)
    {
        cin>>k>>c>>s;
        long long x = power(k,c-1);
        printf("Case #%d: ",num);
        for(int i=0;i<k;i++)
            cout<< (1 + (i*x))*1LL<<" ";
        cout<<"\n";
        ++num;
    }
}
