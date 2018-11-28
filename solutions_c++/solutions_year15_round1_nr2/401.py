#include <stdio.h>

int m[1100];
int b;
int n;

int calc_n(long long t)
{
    long long ans = 0;
    int i, j, k;
    for(i = 0; i < b; i++)
        ans += t / m[i] + 1;
    if(ans > (1<<30))
        return (1<<30);
    else
        return (int)ans;
}

int calc_i(long long t, int rest)
{
    int i, j, k;
    for(i = b-1; i >= 0; i--)
        if (t % m[i] == 0){
            if(rest > 0)
                rest--;
            else
                return i;
            }
}

int solve()
{
    int ans;
    scanf("%d%d", &b, &n);
    //n--;
    int i, j, k;
    for(i = 0; i < b; i++)
        scanf("%d", &m[i]);
    long long tmin, tmax, tmid;
    tmin = 0; tmax = ((long long)1)<<60;
    while (tmin < tmax){
        tmid = (tmin + tmax) >> 1;
        k = calc_n(tmid);
        if(k < n)
            tmin = tmid + 1;
        else
            tmax = tmid;
        }
    k = calc_n(tmin);
    ans = calc_i(tmin, k - n);

    return ans+1;
}

int main()
{
    int t, t0;
    scanf("%d", &t);
    for(t0 = 0; t0<t; t0++){
        printf("Case #%d: %d\n", t0 + 1, solve());
        }
    return 0;
}
