#include <stdio.h>
#include <algorithm>
using namespace std;


double naom[2000],ken[2000];
bool used[2000];

int main()
{
    int t;
    scanf("%d",&t);
    for (int l=1;l<=t;l++)
    {
        printf("Case #%d: ",l);

        int n;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            scanf("%lf",&naom[i]);
        for (int i=0;i<n;i++)
            scanf("%lf",&ken[i]);

        sort(naom,naom+n);
        sort(ken,ken+n);
        for (int i=0;i<n;i++) used[i] = false;
        
        int j0 = 0;
        int ans1 = 0, ans2 = 0;
        for (int i=n-1;i>=0;i--)
        {
            int j;
            for (j=j0;j<n; j++) 
            {
                if ( !used[j] && ken[j] > naom[i] ) break;
            }
            if ( j == n )
            {
                  used[j0++] = true;
                  ans2++;
            }
           else
           {
              used[j] = true;
           }
        }
        /*
        for (int i=0;i<n;i++) printf("%lf ",naom[i]);
        putchar('\n');
        for (int i=0;i<n;i++) printf("%lf ",ken[i]);
        putchar('\n');
        */
        int j = 0;
        int i = 0;
        while ( i<n && j< n )
        {
            while ( i < n && ken[j] > naom[i] ) i++;
            if ( i<n ) ans1++;
            i++;
            j++;
        }
           
        printf("%d %d\n",ans1,ans2);
    }
}
