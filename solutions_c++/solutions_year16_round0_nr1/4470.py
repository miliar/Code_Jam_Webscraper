#include <bits/stdc++.h>
using namespace std;


typedef long long LL;

int db[10];
int dbc=0;



inline void db_clear()
{
    dbc=0;
    for(int i=0;i<=9;i++)db[i]=0;
}

inline bool db_add(int x)
{
    if(db[x]==0)
    {
        db[x]=1;
        dbc++;
    }
    return (dbc==10) ;
}

inline bool db_add_n(LL n)
{
    while(n != 0)
    {
        if (db_add(n%10)) return true;
        n/=10;
    }
    return false;
}

LL check(LL n)
{
    LL s=0;
    db_clear();
    while(1)
    {
        s+=n;
        if(db_add_n(s)) return s;
    }

}


int main()
{
    LL T,x;


    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin>>T;


    for(LL i=1;i<=T;i++)
    {
        scanf("%lld",&x);
        if(x==0)
        {
            printf("Case #%lld: INSOMNIA\n",i);
        }
        else
        {
            printf("Case #%lld: %lld\n",i,check(x));
        }
    }

}
