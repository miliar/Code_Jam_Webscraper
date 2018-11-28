#include <QCoreApplication>

int main(int argc, char *argv[])
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int caseNumber = 0; caseNumber < T; caseNumber++) {
        int x, y;
        scanf("%d%d", &x, &y);
        printf("Case #%d: ", caseNumber + 1);
        int start = x > 0;
        char dir[] = {'E', 'W'};
        for (int i = 0 ; i < abs(x); i++)
            printf("%c%c", dir[start & 1], dir[start + 1 & 1]);
        start = y > 0;
        char dirr[] = {'N', 'S'};
        for (int i = 0 ; i < abs(y); i++)
            printf("%c%c", dirr[start & 1], dirr[start + 1 & 1]);
        printf("\n");
    }
}
