#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll f(int n)
{
    if (n == 0) return -1;
    
    int nUsed = 0;
    bool used[10] = {};
    
    int mult = 1;
    while (true)
    {
        ll x = n * (ll)mult;
        assert(x < 1e16);
        
        while (x)
        {
            if (!used[x % 10]) nUsed++;
            used[x % 10] = true;
            x /= 10;
        }
        
        if (nUsed == 10) break;
        
        mult++;
    }
    
    return n * (ll)mult;
}

void solve(int caseId)
{
    int n;
    scanf("%d", &n);
    
    ll value = f(n);
    printf("Case #%d: ", caseId);
    if (value >= 0)
        printf("%lld\n", value);
    else
        printf("INSOMNIA\n");
}

int main()
{
    //for (int i = 1; i <= (int)1e6; i++)
    //    printf("%d -> %lld\n", i, f(i));
    
    int nt;
    scanf("%d", &nt);
    
    for (int i = 0; i < nt; i++)
        solve(i + 1);
    
    return 0;
}
