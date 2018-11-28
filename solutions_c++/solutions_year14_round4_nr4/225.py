#include <cstdio>
#include <string>
#include <vector>
#include <set>
using namespace std;

int M, N;
char buf[100][100];
vector<int> ss[32];
int ans1, ans2;


int f2(vector<int>& v)
{
    set<string> table;
    for(int i = 0; i < v.size(); i++)
        for(int j = 0; !j || buf[v[i]][j - 1]; j++)
        {
            char c = buf[v[i]][j];
            buf[v[i]][j] = 0;
            table.insert(buf[v[i]]);
            buf[v[i]][j] = c;
        }
    return table.size();
}

void f(int n)
{
    if(n < M)
    {
        for(int i = 0; i < N; i++)
        {
            ss[i].push_back(n);
            f(n + 1);
            ss[i].pop_back();
        }
    }
    else
    {
        int alc = 0;
        for(int i = 0; i < N; i++)
            alc += f2(ss[i]);
        if(alc > ans1)
            ans1 = alc, ans2 = 1;
        else if(alc == ans1)
            ans2++;
        
        
 
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++)
    {
        printf("Case #%d: ", tt);
        scanf("%d%d", &M, &N);
        for(int i = 0; i < M; i++)
            scanf("%s", buf[i]);
        ans1 = 0, ans2 = 0;
        f(0);
        printf("%d %d\n", ans1, ans2);
    }
    return 0;
}
