
#include <iostream>
#include <set>
#include <cstdio>
using namespace std;
#define FROM_FILE
#define SMALL_INPUT_FNAME "B-large.in"
#define OUTPUT_FNAME "big_output.txt"

int main()
{
    #ifdef FROM_FILE
        freopen(SMALL_INPUT_FNAME, "r", stdin);
        freopen(OUTPUT_FNAME, "w", stdout);
    #endif // FROM_FILE

    int caseNum;
    scanf("%d", &caseNum);
    for (int T = 1; T <= caseNum; ++T) {
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        double min_time = X / 2.0;
        double cur_min = min_time;
        int i = 1;
        double F_buy = 0;
        do {
           min_time = cur_min;
           F_buy = F_buy + (C / (2 + (i - 1)* F));
           cur_min = F_buy + X / (2 + i * F);
           i++;
        } while(cur_min < min_time);
        printf("Case #%d: %.7lf\n", T, min_time);
    }
    return 0;
}
