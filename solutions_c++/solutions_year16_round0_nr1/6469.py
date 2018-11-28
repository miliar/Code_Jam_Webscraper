#include<bits/stdc++.h>
#define MAX 1e5
using namespace std;
typedef long long ll;
int mask;
bool update(ll x)
{
    while(x>0)
    {
        mask |= 1<<(x%10);
        x/=10;
    }
    return mask==(1<<10)-1;
}
int main()
{
    int n, test, i;
    scanf("%d", &test);
    for(int te=1;te<=test;te++)
    {
        scanf("%d", &n);
        bool f=0;
        mask=0;
        for(i=1;i<=MAX;i++)
        {
            ll num = 1ll*i*n;
            f|=update(num);
            if(f) break;
        }
        if(f)
            cout<<"Case #"<<te<<": "<<1ll*i*n<<endl;
        else
            cout<<"Case #"<<te<<": INSOMNIA"<<endl;    
    }
}

