#include <cstdio>
#include <cstring>
#include <vector>
#include <cstring>
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
using namespace std;
int main()
{
	FILE* fin = freopen("in.txt","rt", stdin);
    FILE* fout = freopen("out.txt","wt", stdout);
	int c;
	scanf("%d",&c);
	FOR(xx,0,c)
	{
        int s;
        char sl[1010];
        memset(sl, 0, sizeof(sl));
        scanf("%d %s", &s, sl);
        int residual = sl[0]- '0';
        int ret = 0;
        FOR(i,1,s+1)
        {
            if (residual < i)
            {
                ret += (i - residual);
                residual += (i - residual);
            }
            residual += sl[i] - '0';
        }
        printf("Case #%d: %d\n", xx + 1, ret);
	}
    fclose(fout);
	fclose(fin);
	return 0;
}