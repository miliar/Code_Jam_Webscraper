#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
    int tt,t=1;
    scanf("%d",&tt);
    while(t<=tt)
    {
        int n;
        int m[1010];
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&m[i]);
        }
        int a1 = 0;
        int a2 = 0;
        int div = 0;
        for(int i=1;i<n;i++)
        {
            if(m[i]<m[i-1]) a1+=m[i-1]-m[i];
            div = max(div,m[i-1]-m[i]);
        }
        for(int i=0;i<n-1;i++)
        {
            if(m[i]>div) a2+=div;
            else a2+=m[i];
        }
        printf("Case #%d: %d %d\n",t++,a1,a2);
    }
    return 0;
}
