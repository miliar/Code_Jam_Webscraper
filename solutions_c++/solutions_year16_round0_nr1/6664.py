#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define MOD 1000000007
ll ans[1000001];
void update(ll num, int A[], int& C)
{
    while(num)
    {
        int rem = num%10;
        num /= 10;
        if(A[rem] == 0)
        {
            A[rem] = 1;
            C++;
        }
    }
}
ll findNum(int N)
{
    int A[10] = {0};
    int C = 0;
    ll i = 1;
    while(C < 10)
    {
        update(i*N,A,C);
        if(C == 10) break;
        i++;
    }
    ans[N] = i*N;
}
int main()
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    for(int i = 1; i <= 1000000; i++)
        findNum(i);
    int T,N;
    scanf("%d",&T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%d",&N);
        printf("Case #%d: ",t);
        if(ans[N] == 0) printf("INSOMNIA\n");
        else printf("%lld\n",ans[N]);
    }
    #ifndef ONLINE_JUDGE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}
