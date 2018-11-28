#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases;
    int map[102][102];
    int ans;
    int i,j;
    int n,m;
    int t;
    int hang[102];
    int lie[102];
    scanf("%d",&cases);
    t=1;
    while(cases--)
    {
        printf("Case #%d: ",t);
        t++;
        scanf("%d%d",&n,&m);
        ans=0;
        memset(hang,0,sizeof(hang));
        memset(lie,0,sizeof(lie));
        for(i=0;i<n;++i)
        {
            for(j=0;j<m;++j)
            {
                scanf("%d",&map[i][j]);
                if(map[i][j]>hang[i])
                {
                    hang[i]=map[i][j];
                }
            }
//            cout<<"hang["<<i<<"]="<<hang[i]<<endl;
        }
        for(i=0;i<m;++i)
        {
            for(j=0;j<n;++j)
            {
                if(map[j][i]>lie[i])
                {
                    lie[i]=map[j][i];
                }
            }
//            cout<<"lie["<<i<<"]="<<lie[i]<<endl;
        }
        for(i=0;i<n;++i)
        {
            if(ans)
                break;
            for(j=0;j<m;++j)
            {
                if(ans)
                    break;
                if(hang[i]>map[i][j]&&lie[j]>map[i][j])
                {
//                    cout<<"i="<<i<<" j="<<j<<endl;
                    ans=1;
                }
            }
        }
        if(ans)
            printf("NO\n");
        else
            printf("YES\n");
    }
    return 0;
}
