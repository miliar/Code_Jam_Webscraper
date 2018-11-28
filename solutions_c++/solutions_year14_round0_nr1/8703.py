#include <iostream>
#include <cstring>
#include <stdio.h>
using namespace std;

char bad[] = "Bad magician!";
char cheat[] = "Volunteer cheated!";

#define N 4

int T;

int row1, row2;
int a[N][N];
int b[N][N];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

    scanf("%d",&T);

    for (int t = 1; t <= T; ++t) {
        int answer = -2;

        scanf("%d",&row1);
        row1--;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                scanf("%d",&a[i][j]);

        scanf("%d",&row2);
        row2--;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                scanf("%d",&b[i][j]);

        for (int first = 0; first < N; ++first)
            for (int second = 0; second < N; ++second) {
                if ( a[row1][first] == b[row2][second] ) {
                    if ( answer != -2 ) answer = -1;
                    else answer = a[row1][first];
                }
            }

        printf("Case #%d: ",t);
        if (answer == -2) {
            printf("%s",cheat);
        }
        else if (answer == -1) {
            printf("%s",bad);
        }
        else {
            printf("%d",answer);
        }
        printf("\n");
    }


    return 0;
}
