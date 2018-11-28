#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<cmath>
#include<cstring>
using namespace std;
int s[10000001];
int c[10000001];
int palin(long long a)
{
    vector<int> x;
    while(a)
    {
        int temp=(a%10);
        x.push_back(temp);
        a/=10;
    }
    int j=x.size()-1;
    for(int i=0;i<x.size()/2;i++,j--)
    {
        if(x[i]==x[j]);
        else return 0;
    }
    return 1;
}
int main()
{
    int t;
    long long a,b;
    scanf("%d",&t);
    long long x=0;

    while(t--)
    {
        x++;
        scanf("%lld",&a);
        scanf("%lld",&b);
        int temp1=a,temp2=b,ans=0;
        for(long long int i=a;i<=b;i++)
        {
            double temp=sqrt(i);
            if(floor(temp)==ceil(temp))//perfect sqr
            {
                if(palin(i) && palin(temp))
                {
                    //cout<<temp<<" "<<i<<endl;
                    ans++;
                }
            }
        }
        printf("Case #%lld: %lld\n",x,ans);
    }
    return 0;
}
