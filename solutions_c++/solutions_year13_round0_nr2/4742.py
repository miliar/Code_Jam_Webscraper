/*  Google Codejam Qualification Round 2013
 *  B Lawnmower
 *  Varot Premtoon 13 Apr 2556
 */

#include <cstdio>
#include <algorithm>

using namespace std;

int sol(int cse)
{
    int n,m;
    int i,j,k;
    int tab[200][200];
    int row[200];
    int col[200];
    scanf("%d %d\n",&n,&m);
    for(i=0;i<200;i++) row[i] = col[i] = 0;
    for(i=0;i<n;i++) for(j=0;j<m;j++) {
        scanf("%d",&tab[i][j]);
        row[i] = max(row[i],tab[i][j]);
        col[j] = max(col[j],tab[i][j]);
    }
    for(i=0;i<n;i++) for(j=0;j<m;j++) {
        if(tab[i][j]<row[i] and tab[i][j]<col[j]) {
            printf("Case #%d: NO\n",cse);
            return 0;
        }
    }
    printf("Case #%d: YES\n",cse);
    return 0;
}

int main()
{
    int t;
    scanf("%d",&t);
    for(int cse=1;cse<=t;cse++) sol(cse);
    return 0;
}
