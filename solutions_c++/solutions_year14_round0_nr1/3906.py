#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,n1,n2,a[4][4],b[4][4],i,j,p = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n1);
        n1--;
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++)
                scanf("%d", &a[i][j]);
        }
        scanf("%d", &n2);
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++)
                scanf("%d", &b[i][j]);
        }
        n2--;
        vector <int> v;
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++) {
                if (a[n1][i] == b[n2][j])
                    v.push_back(a[n1][i]);
            }
        }
        printf("Case #%d: ", ++p);
        if (v.size() == 0)
            printf("Volunteer cheated!\n");
        else if (v.size() > 1)
            printf("Bad magician!\n");
        else
            printf("%d\n", v[0]);
    }
    return 0;
}
