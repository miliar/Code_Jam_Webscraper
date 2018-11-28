#include<iostream>
#include<cstdio>
#include<memory.h>
using namespace std;
int c[10];
bool check()
{
    for(int i=0;i<10;i++)
    {
        if(!c[i])
            return false;
    }
    //cout<<"yes"<<endl;
    return true;
}

int main()
{
    freopen("c:/A-large.in","r",stdin);
    freopen("c:/A-large.out","w",stdout);
    long long  t,n,temp,j=1;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        memset(c,0,sizeof(c));

        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }

        j=n;
        while(!check())
        {
            temp=n;
            while(temp){
                   // cout<<temp<<" ";
                c[temp%10]=1;
                temp/=10;
            }
           // cout<<endl;
            n+=j;
        }

        printf("Case #%d: %lld\n",i,n-j);
    }
    return 0;
}
