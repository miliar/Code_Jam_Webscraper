#include <cstdio>

using namespace std;

char v[1010];

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test,n;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        scanf("\n%d %s",&n,v);
        int s=0,sol=0;
        for(int i=0;i<=n;i++)
        {
            int x=v[i]-'0';
            if(!x) continue;
            if(s<i)
            {
                sol+=i-s;
                s+=i-s;
            }
            s+=x;
        }
        printf("Case #%d: %d\n",t,sol);
    }
    return 0;
}
