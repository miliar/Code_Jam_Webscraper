#include<stdio.h>
#include<algorithm>

using namespace std;

const int MAX = 123;

int T;
int mp[MAX][MAX];
int N,M;
int h[MAX],v[MAX];

void aozora()
{
    for(int i=0;i<MAX;i++)
    {
        h[i]=v[i]=0;
    }
}

int main()
{
    freopen("pb.in","r",stdin);
    freopen("pb.out","w",stdout);

    scanf("%d",&T);
    for(int ti=0;ti<T;ti++)
    {
        aozora();
        scanf("%d%d",&N,&M);
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                scanf("%d",mp[i]+j);
            }
        }
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                h[i]=max(h[i],mp[i][j]);
                v[j]=max(v[j],mp[i][j]);
            }
        }
        bool ok=1;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {

                if(mp[i][j]!=min(h[i],v[j]))
                {
                    ok=0;
                    break;
                }
            }
            if(!ok)
            {
                break;
            }
        }
        printf("Case #%d: ",ti+1);
        if(ok)
        {
            puts("YES");
        }else
        {
            puts("NO");
        }
    }

}
