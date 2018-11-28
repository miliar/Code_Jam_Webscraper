#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;

int N;
int s[2000];

int pos[2000];

int lb[2000];
int rb[2000];


int main()
{
    int T;
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++)
    {
        printf("Case #%d: ", tt);
        scanf("%d", &N);
        map<int, int> t1;
        for(int i = 0; i < N; i++)
            scanf("%d", s + i), t1[s[i]] = 0;
        int cc = 0;
        for(map<int, int>::iterator it = t1.begin(); it != t1.end(); it++)
            it->second = cc++;

        for(int i = 0; i < N; i++)
        {
            s[i] = t1[s[i]];
            pos[s[i]] = i;
        }

        memset(lb, 0, sizeof(lb));
        memset(rb, 0, sizeof(rb));
        for(int i = 0; i < N; i++)
        {
            for(int j = 0; j < i; j++)
                lb[s[i]] += s[j] > s[i];
            for(int j = i + 1; j < N; j++)
                rb[s[i]] += s[j] > s[i];
        }
 
        int ans = 0;
        for(int i = 0; i < N; i++)
            ans += min(lb[i], rb[i]);
        printf("%d\n", ans);
    }
    return 0;
}
