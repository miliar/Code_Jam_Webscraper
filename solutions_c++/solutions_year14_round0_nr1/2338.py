#include<cstdio>

int A[5];

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.txt","w",stdout);
    int t,a,b,te,co,th;
    scanf("%d",&t);
    for ( int x=1 ; x<=t ; x++ )
    {
        co=0;
        scanf("%d",&a);
        for ( int c=1 ; c<=4 ; c++ )
        {
            if ( c == a )
            {
                for ( int d=1 ; d<=4 ; d++ )    scanf("%d",&A[d]);
            }
            else
                for ( int d=1 ; d<=4 ; d++ )    scanf("%d",&te);
        }
        scanf("%d",&b);
        for ( int c=1 ; c<=4 ; c++ )
        {
            if ( c == b )
            {
                for ( int d=1 ; d<=4 ; d++ )
                {
                    scanf("%d",&te);
                    for ( int e=1 ; e<=4 ; e++ )
                    {
                        if ( te == A[e] )
                        {
                            co++;
                            th = te;
                        }
                    }
                }
            }
            else
                for ( int d=1 ; d<=4 ; d++ )    scanf("%d",&te);
        }
        printf("Case #%d: ",x);
        if ( co == 1 )  printf("%d\n",th);
        else if ( co != 0 ) printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");

    }

}
