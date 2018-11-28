#include <cstdio>
#include <numeric>
using namespace std;

int tr[1000000], N;

bool can(long long goal)
{
    int pos=0;
    for(int i=0; i<3; i++)
    {
        long long sum=0;
        while(true)
        {
            if(pos==N)
                return true;
            if(sum+tr[pos]>goal)
                break;
            sum+=tr[pos];
            pos++;
        }
    }
    return false;
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        int p, q, r, s;
        scanf("%d%d%d%d%d", &N, &p, &q, &r, &s);
        for(int i=0; i<N; i++)
            tr[i]=((1ll*i*p+q)%r+s);
        long long lo=0, hi=1e16;
        while(lo+1<hi)
        {
            long long mid=(lo+hi)/2;
            (can(mid) ? hi : lo) = mid;
        }
        long long sum=accumulate(tr, tr+N, 0LL);
        printf("Case #%d: %.11f\n", t, 1.0*(sum-hi)/sum);
    }
}
