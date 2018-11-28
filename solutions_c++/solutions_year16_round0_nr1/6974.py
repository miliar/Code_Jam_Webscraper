#include<bits/stdc++.h>
#define ll long long int
#define PB push_back
#define F first
#define S second
#define tr(c,i) for(typeof((c).begin())i = (c).begin(); i != (c).end(); i++) 
#define sint(n); scanf("%d",&n);
#define sll(n); scanf("%lld",&n);
#define pint(n); printf ("%d\n",n);
#define pll(n); printf ("%lld\n",n);
#define sst(n); scanf("%s",n);
#define pst(n); printf ("%s\n",n);
#define f(i,a,b) for(ll i=a;i<b;i++)
#define set(a,b) memset(a, b, sizeof(a))


using namespace std;

ll arr[10], sum;

void update(ll x)
{
    ll tmp;
    while (x>0)
    {
        tmp = x%10;
        //cout<<tmp<<endl;
        if (arr[tmp]==0)
        {
            arr[tmp]=1;
            sum++;
        }
        x/=10;
    }
    return;
}

int main()
{
    ll i,t,n;
    sll(t);
    f(test,1,t+1)
    {
        sll(n);
        if (n==0)
        {
            printf("Case #%lld: INSOMNIA\n", test);
            continue;
        }
        sum = 0;    set(arr, 0);
        for (i=1;sum<10;i++)
        {
            update(i*n);
            //cout<<i*n<<" -->  ";
            //f(j,0,10){cout<<arr[i]<<" ";}cout<<endl;
        }
        printf("Case #%lld: %lld\n", test, (i-1)*n);
    }
    return 0;
}
