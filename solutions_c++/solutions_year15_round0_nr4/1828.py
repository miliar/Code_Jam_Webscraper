#include <cstdio>

int X, R, C, A[30][30];

int main()
{
    int T;
    freopen("D1.txt","r",stdin);
    freopen("resD.out","w",stdout);
    scanf("%d", &T);
    for(int t = 1 ; t <= T ; t++ )
    {
        scanf("%d%d%d",&X,&R,&C);
        if( X == 1 ) printf("Case #%d: GABRIEL\n", t);
        else if( X == 2 )
        {
            if( (R * C)&1 ) printf("Case #%d: RICHARD\n", t);
            else printf("Case #%d: GABRIEL\n", t);
        }
        else if( X == 3 )
        {
            if( (R < 3 && C < 3) || ( R==1 || C==1 ) || (R*C)%3 ) printf("Case #%d: RICHARD\n", t);
            else printf("Case #%d: GABRIEL\n", t);
        }
        else if( X == 4 )
        {
            if( R + C >= 7 ) printf("Case #%d: GABRIEL\n", t);
            else printf("Case #%d: RICHARD\n", t);
        }
    }
}
/*
64
2 2 2
2 1 3
4 4 1
3 2 3
2 3 3
3 4 3
1 2 1
3 2 2
4 3 4
4 1 2
3 1 4
4 4 4
3 2 4
2 4 4
4 2 2
1 3 3
3 1 2
2 1 4
4 1 1
2 2 3
1 4 3
2 4 2
4 1 4
4 4 2
3 3 1
2 4 3
1 3 2
1 3 4
1 4 2
1 2 4
2 1 2
1 2 2
3 2 1
4 2 1
3 3 4
4 2 4
1 3 1
1 1 2
2 2 4
2 3 1
1 4 4
1 2 3
1 1 1
4 3 2
2 1 1
3 4 2
3 3 2
3 4 4
4 1 3
2 4 1
1 1 4
2 3 4
3 3 3
2 2 1
3 4 1
1 1 3
4 3 3
2 3 2
4 4 3
3 1 1
4 3 1
3 1 3
4 2 3
1 4 1
*/
