#include <cstdio>
#include <cstring>

int main()
{
    int i, j, t=1, T, x, a, vis[22];
    scanf("%d", &T);
    while(T--)
    {
        memset(vis, 0, sizeof(vis));
        scanf("%d", &x);
        for(i=1; i<=4; i++) for(j=1; j<=4; j++)
        {
            scanf("%d", &a);
            if(i==x) vis[a]++;
        }
        scanf("%d", &x);
        for(i=1; i<=4; i++) for(j=1; j<=4; j++)
        {
            scanf("%d", &a);
            if(i==x) vis[a]++;
        }
        int cnt=0, id;
        for(i=0; i<22; i++) if(vis[i]==2) cnt++, id=i;
        printf("Case #%d: ", t++);
        if(!cnt) printf("Volunteer cheated!\n");
        else if(cnt==1) printf("%d\n", id);
        else printf("Bad magician!\n");
    }
    return 0;
}
