#include <bits/stdc++.h>
#define MAX 500

using namespace std;
int mat1[4][4];
int mat2[4][4];
bool taken[17];

int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, caseno = 0;
    scanf("%d", &t);
    while(t--)
    {
        memset(taken, false, sizeof(taken));
        int ans1, ans2;
        scanf("%d", &ans1);
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                scanf("%d", &mat1[i][j]);
                if(i == ans1 - 1)
                    taken[mat1[i][j]] = true;
            }
        }
        scanf("%d", &ans2);
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                scanf("%d", &mat2[i][j]);
        int cr = ans2 - 1, counter = 0, ans;
        for(int i = 0; i < 4; i++)
        {
            if(taken[mat2[cr][i]])
            {
                counter++;
                ans = mat2[cr][i];
            }
        }
        printf("Case #%d: ", ++caseno);
        if(counter > 1)
            printf("Bad magician!\n");
        else if(counter == 0)
            printf("Volunteer cheated!\n");
        else
            printf("%d\n", ans);

    }

}
