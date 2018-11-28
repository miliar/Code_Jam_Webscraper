#include<stdio.h>
#include<string.h>

int a[10][10],b[10][10];

int main()
{
    freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);

    int T;
    int m,n;
    int num,res;
    scanf("%d",&T);
    for( int kase = 1; kase <= T; ++kase )
    {
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        num = 0;
        scanf("%d",&m);
        for( int i = 1; i <= 4; ++i )
            for( int j = 1; j <= 4; ++j )
            scanf("%d",&a[i][j]);
        scanf("%d",&n);
        for( int i = 1; i <= 4; ++i )
            for( int j = 1; j <= 4; ++j )
            scanf("%d",&b[i][j]);
        for( int i = 1; i <= 4; ++i )
            for( int j = 1; j <= 4; ++j )
                if( a[m][i]==b[n][j] ){num++; res = a[m][i];}
        if( num==0 ) printf("Case #%d: Volunteer cheated!\n",kase);
        if( num>1 )  printf("Case #%d: Bad magician!\n",kase);
        if( num==1 ) printf("Case #%d: %d\n",kase,res);
    }
    return 0;
}
