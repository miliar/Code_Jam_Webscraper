#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

int cards1[10][10];
int cards2[10][10];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int CAS1;
    vector<int> dict;
    scanf("%d", &CAS1);
    for (int CAS=1; CAS<=CAS1; CAS++)
    {
        int a1, a2;
        scanf("%d", &a1);
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
                scanf("%d", &cards1[i][j]);
        scanf("%d", &a2);
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
                scanf("%d", &cards2[i][j]);

        dict.clear();
        for (int i=1; i<=4; i++)
        {
            for (int j=1; j<=4; j++)
                if (cards1[a1][i] == cards2[a2][j])
                {
                    dict.push_back(cards1[a1][i]);
                    break;
                }
        }
        printf("Case #%d: ", CAS);
        if (dict.size()==1)
            printf("%d\n", dict[0]);
        else if (dict.size()==0)
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
