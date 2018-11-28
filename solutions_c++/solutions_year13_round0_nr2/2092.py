#include<stdio.h>

int a[105][105];

int main()
{
    freopen("B.in", "r", stdin);
    freopen("Bout.in", "w", stdout);

    int T, kas=1, i, j, r, c, N, M, flag1, flag2;

    for(scanf("%d",&T); kas<=T; kas++)
    {
        scanf("%d%d",&N,&M);
        for(i=0; i<N; i++)for(j=0; j<M; j++)scanf("%d",&a[i][j]);

        if( N==1 || M==1 ) { printf("Case #%d: YES\n",kas); continue; }

        bool Yes = 1;
        for(i=0; i<N; i++)
            for(j=0; j<M; j++)
            {
                r=i;    c=j;    flag1=0;
                while(r<N && a[i][j]>=a[r][c])r++;
                if(r==N)flag1++;
                r=i; c=j;
                while(r>=0 && a[i][j]>=a[r][c])r--;
                if(r==-1)flag1++;

                r=i;    c=j;    flag2=0;
                while(c<M && a[i][j]>=a[r][c])c++;
                if(c==M)flag2++;
                r=i;    c=j;
                while(c>=0 && a[i][j]>=a[r][c])c--;
                if(c==-1)flag2++;

                if(flag1<2 && flag2<2) { Yes=0; i=N;    break; }
            }

        printf("Case #%d: %s\n",kas,(Yes)?"YES":"NO");
    }

    return 0;
}
