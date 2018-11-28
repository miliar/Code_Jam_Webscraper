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


int main()
{
    ll t;
    sll(t);
    f(test, 1, t+1)
    {
        char s[105];
        sst(s);
        ll len = strlen(s);
        ll changes=0;
        f(i,0,len-1)
        {
            if (s[i]!=s[i+1])
                changes++;
        }
        if (s[len-1]=='-')
            changes++;
        printf("Case #%lld: %lld\n", test, changes);
    }

    return 0;
}
