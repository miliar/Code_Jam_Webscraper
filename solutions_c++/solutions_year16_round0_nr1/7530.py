#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
typedef long long ll;
#define ALL(a) (a).begin(),(a).end()
using namespace std;

void solve(int xx, int n)
{
    if (n == 0)
    {
        printf("Case #%d: INSOMNIA\n", xx + 1);
        return;
    }
    int cnt[10];
    memset(cnt, 0, sizeof(cnt));
    ll nn = 0;
    while(true)
    {
        bool isAll = true;
        nn += n;
        ll t = nn;
        //printf("%lld, ", nn);
        if (nn < 0 )
            printf("shit!!\n");
        while(t != 0)
        {
            cnt[t % 10L] = 1;
            t /= 10L;
        }
            
        FOR(j,0,10)
        {
            if (cnt[j] == 0)
            {
                isAll = false;
                break;
            }
        }
        if (isAll)
        {
            printf("Case #%d: %lld\n", xx + 1, nn);
            break;
        }
    }
}


int main()
{

	FILE* fin = freopen("A-large.in","rt", stdin);
    FILE* fout = freopen("out.txt","wt", stdout);
	int c;
	scanf("%d",&c);
	FOR(xx,0,c)
	{
        int n;
        scanf("%d", &n);
        solve(xx, n);
    }

    //FOR(i,0,1000001)
    //{
    //    solve(i, i);
    //}

    fclose(fout);
	fclose(fin);

	return 0;
}