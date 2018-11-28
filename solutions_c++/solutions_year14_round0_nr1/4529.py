#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

int cas=1;
void work()
{
    set<int> ss;
    int count=0;
    int ans=0;

    int n;
    scanf("%d", &n);
    for(int i=1;i<=4;i++) for(int j=1;j<=4;j++)
    {
        int tmp;
        scanf("%d", &tmp);
        if(i==n) ss.insert(tmp);
    }

    int m;
    scanf("%d", &m);
    for(int i=1;i<=4;i++) for(int j=1;j<=4;j++)
    {
        int tmp;
        scanf("%d", &tmp);
        if(i==m)
        {
            if(ss.count(tmp))
                count++, ans=tmp;
        }
    }

    printf("Case #%d: ", cas++);
    if(count==0)
        puts("Volunteer cheated!");
    else if(count>1)
        puts("Bad magician!");
    else
        printf("%d\n", ans);
}

int main()
{
   // freopen("D:/A-small-attempt0.in", "r", stdin);
   // freopen("D:/out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    while(T--)
        work();
}
