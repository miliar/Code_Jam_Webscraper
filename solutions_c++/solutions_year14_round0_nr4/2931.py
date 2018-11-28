#include <stdio.h>
#include <vector>
#include <algorithm>

#define delta = 0.0000004

std::vector< float > ken;
std::vector< float > naomi;

int BinFindKen(int left, int right, float value){
    int l = left;
    int r = right;

    if (r-l <= 1) return r;
    int m = (l+r)/2;

    if (value < ken[m]) r = m;
    if (value > ken[m]) l = m;

    return BinFindKen(l,r,value);
}

void SolveTestcase(int TestCase){
    int N;
    ken.clear();
    naomi.clear();

    scanf("%d", &N);

    ken.push_back(0.0);
    naomi.push_back(0.0);

    for (int i=1; i<=N; i++){float t; scanf("%f", &t); naomi.push_back(t);}
    for (int i=1; i<=N; i++){float t; scanf("%f", &t); ken.push_back(t);}

    ken.push_back(1.0);
    naomi.push_back(1.0);

    sort(ken.begin(), ken.end());
    sort(naomi.begin(), naomi.end());

    //for (int i=1; i<=N; i++) printf("%.3f ", naomi[i]);  printf("\n");
    //for (int i=1; i<=N; i++) printf("%.3f ", ken[i]);    printf("\n");

    int score_W = 0, score_DW = 0;
    int ken_left = 0, ken_right = N+1, naomi_left = 0, naomi_right = N+1;

    // calculating for War
    for (int j=1; j<=N; j++){
        int m = BinFindKen(ken_left, ken_right, naomi[j]);
        if (m == N+1) score_W++;  // now ken will use the m-th block to defeat naomi
        ken_left = m;
    }
    // calculating for D war

    ken_right = N;
    int naomi_c = 0;
    for (naomi_c = N;naomi_c>0;naomi_c--){
        while (ken[ken_right] > naomi[naomi_c]) ken_right--;
        if (ken_right == 0) break;
        // ken[ken_right] <---> naomi[j];
        ken_right--;
    }
/*
    ken_right = N; naomi_left = 1;
    while (naomi[naomi_left] < ken[ken_right]){
        ++naomi_left;
        --ken_right;
    }
*/
    score_DW = N-naomi_c;

    printf("Case #%d: %d %d\n", TestCase, score_DW, score_W);
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
