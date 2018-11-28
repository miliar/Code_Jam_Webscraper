#include <stdio.h>

void SolveTestcase(int TestCase){

    int ans1, ans2, a1[4], a2[4];
    scanf("%d", &ans1);
    for (int j=0; j<4; j++){
        int a;
        for (int i=0; i<4; i++)
            if (j == ans1-1) scanf("%d", &a1[i]);
                        else scanf("%d", &a);
    }

    scanf( "%d", &ans2);
    for (int j=0; j<4; j++){
        int a;
        for (int i=0; i<4; i++)
            if (j == ans2-1) scanf( "%d", &a2[i]);
                        else scanf( "%d", &a);
    }

    int c = 0;
    int a;
    for (int i=0; i<4; i++)
        for (int k=0; k<4; k++)
            if (a1[i] == a2[k]){c++; a = a1[i];};

    if (c == 0) printf("Case #%d: Volunteer cheated!\n", TestCase);
    if (c == 1) printf("Case #%d: %d\n", TestCase, a);
    if (c >= 2) printf("Case #%d: Bad magician!\n", TestCase);
}


int main(){
    int T;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; testcase++)
        SolveTestcase(testcase);

    fclose(stdin);
    fclose(stdout);
    return 0;
}
