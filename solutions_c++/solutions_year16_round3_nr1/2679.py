#include<cstdio>

using namespace std;


// for qsort
/*
int compare(int *t, int *s) {
    return *t - *s;
}
*/

int N;
int P[26];

void solve() {
    int total = 0;
    int max = 0;
    for(int i = 0; i < N; ++i) {
        total += P[i];
        if(P[i]>P[max]) max = i;
    }
    if(total % 2) {
        printf(" %c", max+'A');
        --total;
        P[max]--;
    }


    int second;
    int sec_val;
    for(; total; total-=2) {
        max = 0; second = 0;
        sec_val = P[0]-1;
        for(int i = 1; i < N; ++i) {
            if(P[max] < P[i]) {
                sec_val = P[max];
                second = max;
                max = i;
                if(sec_val < P[max]-1) {
                    second = max;
                    sec_val = P[max]-1;
                }
            }
            else if(sec_val < P[i]) {
                second = i;
                sec_val = P[i];
            }
            //printf("%d %d %d\n", max, second, sec_val);
        }
        P[max]--;
        P[second]--;
        printf(" %c%c", max+'A', second+'A');
        //for(int i = 0; i < N; ++i) {
        //    printf(" %d", P[i]);
        //}
        //printf("\n");
    }
}

void solve_and_print() {
    scanf("%d", &N);
    for(int i = 0; i < N; ++i) {
        scanf("%d", P+i);
    }
    solve();
    printf("\n");
}


int main() {
    int dataset_num, case_num;

    scanf("%d", &dataset_num);
    for(case_num = 1; case_num <= dataset_num; ++case_num) {
        printf("Case #%d:", case_num);

        solve_and_print();
    }

    return 0;
}
