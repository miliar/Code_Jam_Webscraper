#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<set>
using namespace std;
int a1[10][10], a2[10][10];
set <int>  s;
set <int> ::iterator it;
int main()
{
	freopen("F:in.txt","r",stdin);
	freopen("F:Out.txt","w",stdout);
    int T, r1, r2, cas  = 0, i, j;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&r1);
        s.clear();
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                scanf("%d",&a1[i][j]);
        scanf("%d",&r2);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                scanf("%d",&a2[i][j]);
        for(j = 1; j <= 4; j++)
        {
            for(i  = 1; i <= 4; i++)
            {
                if(a1[r1][i] == a2[r2][j])
                    s.insert(a1[r1][i]);
            }
        }
        printf("Case #%d: ",++cas);
        if(s.size() == 0)
            printf("Volunteer cheated!\n");
        else if(s.size() == 1)
        {
            it = s.begin();
            printf("%d\n",*it);
        }
        else
            printf("Bad magician!\n");
    }
    return 0;
}
