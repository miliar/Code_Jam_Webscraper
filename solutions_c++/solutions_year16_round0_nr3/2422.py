#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
typedef long long lint;

lint T, n, m;
lint num[10+5], d[10+5];

lint Base(lint x, lint k)
{
    lint ret=0, tmp=1;
    while(x)
    {
        ret+=tmp*(x&1);
        x>>=1;
        tmp*=k;
    }
    return ret;
}

bool Prime(lint x, lint j)
{
    for(lint i=2; i*i<=x; i++)
        if(!(x%i))  
        {
            d[j]=i;
            return false;
        }
    return true;
}

bool Judge()
{
    for(lint j=2; j<=10; j++)
        if(Prime(num[j], j))    return false;
    return true;
}

void Put(lint x)
{
    while(x)
    {
        cout<<(x&1);
        x>>=1;
    }
    return ;
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("gcj3.out", "w", stdout);
    
    cin>>T>>n>>m;
    printf("Case #1:\n");

    lint a=(1<<(n-1))+1, b=(1<<n)-1;
    for(lint i=a; i<=b&&m; i+=2)
    {
        for(lint j=2; j<=10; j++)    num[j]=Base(i, j);

        if(Judge())
        {
            --m;
            cout<<num[10];
            for(lint j=2; j<=10; j++)    cout<<' '<<d[j];
            printf("\n");
        }
    }
    return 0;
}
