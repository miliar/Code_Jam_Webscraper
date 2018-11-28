#include <bits/stdc++.h>
#define PB push_back
#define FT first
#define SD second
#define MP make_pair
#define INF 0x3f3f3f3f
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int>  P;
const int N = 1e5 + 10,MOD = 7+1e9;
char ss[N];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T, ca = 0;
    scanf("%d", &T);
    while(T --) {
        scanf("%s", ss);
        int len = strlen(ss);
        int cnt = 0;
        for(int i = 0;i < len;) {
            int j = i;
            while(j < len && ss[j] == ss[i]) j ++;
            cnt ++, i = j;
        }
        if(ss[len - 1] == '+') cnt --;
        printf("Case #%d: %d\n", ++ ca, cnt);
    }
    return 0;
}