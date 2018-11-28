 //FUCK

#include<stdio.h>

int map[200][200];
long long ret;

void init()
{
    for(int i=0;i<200;i++)
    {
        for(int j=0;j<200;j++)
        {
            map[i][j]=0;
        }
    }
    ret=0;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
    int t,n,m;

    scanf("%d",&t);
    for(int tt=0;tt<t;tt++)
    {
        init();
        scanf("%d %d",&n,&m);
        for(int i=0;i<m;i++)
        {
            int a,b,c;
            scanf("%d %d %d",&a,&b,&c);
            a--;
            b--;
            map[a][b]+=c;
        }

        for(int i=0;i<n;i++)
        {
            for(int j=n-1;j>=0;j--)
            {
                if(map[i][j])
                {
                    for(int k=0;k<i;k++)
                    {
                        for(int l=i;l<j;l++)
                        {
                            if(map[i][j]<=map[k][l])
                            {
                                map[k][l]-=map[i][j];
                                map[i][l]+=map[i][j];
                                map[k][j]+=map[i][j];
                                ret+=(map[i][j])*(i-k)*(j-l);
                                map[i][j]=0;
                                goto out;
                            }
                            else
                            {
                                map[i][j]-=map[k][l];
                                map[i][l]+=map[k][l];
                                map[k][j]+=map[k][l];
                                ret+=(map[k][l])*(i-k)*(j-l);
                                map[k][l]=0;
                            }
                        }
                    }
                }
out:            int sssssssssss;
            }
        }

        printf("Case #%d: %lld\n",tt+1,ret);
    }
}
