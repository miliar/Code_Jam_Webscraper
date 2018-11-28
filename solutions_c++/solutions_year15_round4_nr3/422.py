#include <cstdio>
#include <unordered_map>
#include <string>
#include <vector>
using namespace std;
unordered_map<string, int> m;
vector<int> rec[21];
int a[60000];
char buf[100];

void solve(int tp)
{
    int n;
    scanf("%d",&n);
    for(int i = 0; i < 21; i++)
        rec[i].clear();
    int k1 = 0;
    m.clear();
    for(int i = 0; i < n; i++)
    {
        char c = ' ';
        while(c== ' ')
        {
            scanf("%s",buf);
            if (m.find(string(buf)) == m.end())
                m[string(buf)] = k1++;
            rec[i].push_back(m[string(buf)]);
            scanf("%c",&c);
        }
    }
    int sol = 1000000;
    for(int i = 0; i < (1<<n); i++)
    {
        if (!(i & 1))
            continue;
        if ((i & 2))
            continue;
        for(int j = 0; j < k1; j++)
            a[j] = 0;
        for(int j = 0; j < n; j++)
        {
            for(int k = 0; k < rec[j].size(); k++)
            {
                if (i & (1 << j))
                    a[rec[j][k]] |= 1;
                else
                    a[rec[j][k]] |= 2;
            }
        }
        int num = 0;

        for(int j = 0; j < k1; j++)
        {
            if (a[j]== 3)
                num ++;
        }
        if (num < sol)
        {
            sol = num;
        }
    }
    printf("Case #%d: %d\n",tp,sol);
}

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i= 1; i <= t; i++)
        solve(i);
    return 0;
}
