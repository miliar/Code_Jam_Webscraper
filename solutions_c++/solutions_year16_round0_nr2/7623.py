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
int main()
{
	FILE* fin = freopen("B-large.in","rt", stdin);
    FILE* fout = freopen("out.txt","wt", stdout);

	int c;
	scanf("%d",&c);
	FOR(xx,0,c)
	{
        char tmp[200];
        memset(tmp, 0, sizeof(tmp));
        scanf("%s", tmp);
        int cnt = 1;
        FOR(i,1,strlen(tmp))
        {
            if (tmp[i-1] != tmp[i])
                cnt++;
        }
        if (tmp[strlen(tmp) - 1] == '+')
            cnt--;
        printf("Case #%d: %d\n", xx + 1, cnt);
	}
    fclose(fout);
	fclose(fin);
	return 0;
}