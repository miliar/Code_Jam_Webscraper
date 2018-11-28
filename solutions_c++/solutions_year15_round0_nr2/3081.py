# include<cstdio>
# include<algorithm>
# include<iostream>
# include<cstring>
# include<string>
# include<cmath>
# include<queue>

# define N 1010
# define M 100010

typedef long long ll;

using namespace std;

int n;
int p[N];

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.out","w",stdout);
    int T;scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d",&n);
        int maxv=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&p[i]);
            maxv=max(p[i],maxv);
        }
        int global=maxv;
        for(int i=1;i<=maxv;i++)
        {
            int local=i;
            for(int j=0;j<n;j++)
            {
                local+=(p[j]-1)/i;
            }
            global = min(local,global);
        }
        printf("Case #%d: %d\n",t,global);
    }
    return 0;
}

