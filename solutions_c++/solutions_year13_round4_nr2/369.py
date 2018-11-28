#include <cstdio>
#include <algorithm>
using namespace std;

long long int gap[52];
int n;
long long int p;

int main()
{
    gap[0] = 1;
    for(int i=1; i<=51; ++i) gap[i] = gap[i-1]*2;
    int T;
    scanf("%d", &T);
    for(int cnt = 1; cnt<=T; ++cnt)
    {
        scanf("%d %lld", &n, &p);
        printf("Case #%d: ", cnt);
        int i;
        long long int now = 1;
        for(i=0; now+gap[n-1-i]<=p; ++i) now+=gap[n-1-i];
        printf("%lld ", min(gap[n]-1, gap[i+1]-2));
        for(i=0; gap[n-i]>p; ++i);
        printf("%lld\n", gap[n]-gap[i]);
    }
    return 0;
}
