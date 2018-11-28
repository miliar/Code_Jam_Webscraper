#include <cstdio>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    freopen(argv[1], "r", stdin);
    freopen("output.txt", "w", stdout);

    int total_cases;
    scanf("%d", &total_cases);

    for (auto i = 0; i < total_cases; ++i)
    {
        int arr_1[4][4];
        int arr_2[4][4];
        int choice_1;
        int choice_2;
        
        vector<int> matches;

        scanf("%d", &choice_1);
        choice_1 -= 1;
        scanf("%d %d %d %d", &arr_1[0][0], &arr_1[0][1], &arr_1[0][2], &arr_1[0][3]);
        scanf("%d %d %d %d", &arr_1[1][0], &arr_1[1][1], &arr_1[1][2], &arr_1[1][3]);
        scanf("%d %d %d %d", &arr_1[2][0], &arr_1[2][1], &arr_1[2][2], &arr_1[2][3]);
        scanf("%d %d %d %d", &arr_1[3][0], &arr_1[3][1], &arr_1[3][2], &arr_1[3][3]);

        scanf("%d", &choice_2);
        choice_2 -= 1;
        scanf("%d %d %d %d", &arr_2[0][0], &arr_2[0][1], &arr_2[0][2], &arr_2[0][3]);
        scanf("%d %d %d %d", &arr_2[1][0], &arr_2[1][1], &arr_2[1][2], &arr_2[1][3]);
        scanf("%d %d %d %d", &arr_2[2][0], &arr_2[2][1], &arr_2[2][2], &arr_2[2][3]);
        scanf("%d %d %d %d", &arr_2[3][0], &arr_2[3][1], &arr_2[3][2], &arr_2[3][3]);

        
        for (auto j = 0; j < 4; ++j)
        {
            for (auto k = 0; k < 4; ++k)
            {
                if(arr_1[choice_1][j] == arr_2[choice_2][k])
                {
                    matches.push_back(arr_1[choice_1][j]);
                }
            }
        }

        switch(matches.size())
        {
            case 0:
                printf("Case #%d: %s\n", i+1, "Volunteer cheated!");
                break;
            case 1:
                printf("Case #%d: %d\n", i+1, matches[0]);
                break;
            default:
                printf("Case #%d: %s\n", i+1, "Bad magician!");
                break;
        }
    }
}
