#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<utility>

inline void fill(long long N, int& stat, int& ans, int target)
{
    long long pow = 1LL;
    long long res = 0LL;
    while(pow <= N) pow = (pow<<3) + (pow<<1);
    pow /= 10LL;
    //printf("%d %d\n", pow, N);
    while(pow>0)
    {
        res = N/pow;
        stat |= (1<<(int)res);
        ans++;
        if(stat == target)
            return;
        N=N%pow;
        pow/=10LL;        
    }
}

int count(long long N)
{
    if(N == 0LL) return -1;
    int ans = 0;
    int stat = 0;
    int target = (1<<10) - 1;
    long long temp = N;
    
    while(stat != target)
    {
        //printf("%ox %ox\n", stat, target);
        fill(temp, stat, ans, target);
        if(stat == target)
            break;
        temp+=N;
        
    }
    return temp;
}
/*
int main()
{
    for(int i=0;i<201;++i)
        printf("%d\n", count(i));
}
*/
int main()
{
    int T;
    long long N;
    scanf("%d", &T);
    for(int i=1;i<T+1;++i)
    {
        scanf("%lld", &N);
        int ans = count(N);
        printf("Case #%d: ", i);
        if(ans == -1)
            printf("INSOMNIA\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}

