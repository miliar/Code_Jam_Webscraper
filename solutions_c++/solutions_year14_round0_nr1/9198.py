#include <cstdio>

using namespace std;

int a[20];

int main()
{
    int t,i,j,ii,row,x,ans;
    scanf ("%d",&t);
    for ( ii=1; ii<=t; ii++ )
    {
        ans = -1;
        for ( i=1; i<=16; i++ ) a[i] = 0;
        scanf ("%d",&row);
        for ( i=1; i<=4; i++ )
            for ( j=1; j<=4; j++ )
            {
                scanf ("%d",&x);
                if ( i == row ) a[x] = 1;
            }
        
        scanf ("%d",&row);
        for ( i=1; i<=4; i++ )
            for ( j=1; j<=4; j++ )
            {
                scanf ("%d",&x);
                if ( i == row ) a[x]++;
                if ( a[x] == 2 )
                {
                    if ( ans == -1 ) ans = x;
                    else ans = -2;
                }
            }
        if ( ans == -1 ) printf ("Case #%d: Volunteer cheated!\n",ii);
        else if ( ans == -2 ) printf ("Case #%d: Bad magician!\n",ii); 
        else printf ("Case #%d: %d\n",ii,ans);
    }
}