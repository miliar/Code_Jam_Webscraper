// RandomUsername (Nikola Jovanovic)
// Google Code Jam 2015
// Round 1A
// B

#include <bits/stdc++.h>
#define MAXB 1005
#define lld long long
#define ff(i,a,b) for(int i=a; i<=b; i++)
#define fb(i,a,b) for(int i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2

using namespace std;

lld n, t, b;
lld a[MAXB];

lld done(lld t)
{
    lld ret = 0;
    ff(i, 1, b)
    {
        ret += (lld)(ceil(1.0 * t / a[i]));
    }
    return ret;
}

int main()
{
    freopen("Bin.txt","r",stdin);
    freopen("Bout.txt", "w", stdout);

    scanf("%lld", &t);
    for(lld tt = 1; tt <= t; tt++)
    {
        scanf("%lld %lld", &b, &n);
        for(lld i = 1; i <= b; i++)
        {
            scanf("%lld", &a[i]);
        }
        //ae
        lld hi = 1000000000000000LL;
        lld lo = 0;
        lld pivot;
        while(hi > lo)
        {
            pivot = (hi + lo) / 2;
            if(hi - lo == 1) pivot++;
            if(done(pivot) < n)
                lo = pivot;
            else
                hi = pivot - 1;
           // cout<<pivot<<" "<<done(pivot)<<endl;
        }
        lld val = done(hi);
        hi++;
        lld dif = n - val;
       // cout<<dif<<" "<<hi<<endl;
        //hi++;
       // cout << dif << endl;
        for(lld i = 1; i <= b; i++)
        {
            if( (hi-1) % a[i] == 0)
                dif--;
            if(dif == 0)
            {
                printf("Case #%lld: %lld\n", tt, i);
                break;
            }
        }
    }
    return 0;
}
