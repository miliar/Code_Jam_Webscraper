#include<bits/stdc++.h>
using namespace std;

typedef long long int ll ;

long long int getNext(long long int x)
{
    int num[20]= {0} ;
    for(int i=1 ;  ; i++)
    {
        ll temp = i*x ;
        while(temp>0)
        {
            num[temp%10]=1 ;
            temp=temp/10 ;
        }
        int flag=1 ;
        for(int k=0 ; k<10 ; k++)
        {
            if(num[k]==0)
            {
                flag=0 ;
                break ;
            }
        }
        if(flag==1)
        {
            return i*x ;
        }
    }
}


int main()
{
    freopen("A-large.in","r",stdin) ;
    freopen("AlargeF.out","w",stdout) ;
    int t ;
    scanf("%d",&t) ;
    int z=1 ;
    while(t--)
    {
        ll n ;
        scanf("%lld",&n) ;
        //cout << n << " " ;
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",z) ;
        }
        else
        {
            ll r=getNext(n) ;
            printf("Case #%d: %lld\n",z,r) ;
        }
        z++ ;
    }
    return 0 ;
}
