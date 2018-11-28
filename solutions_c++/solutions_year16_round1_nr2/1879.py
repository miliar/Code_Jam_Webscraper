#include<cstdio>

using namespace std;


int N;
int height[2501];


void solve_and_print() {
    scanf("%d", &N);
    for(int i = 1; i < 2501; ++i) {
        height[i] = 0;
    }
    for(int i = 0; i < 2 * N - 1; ++i) {
        int t;
        for(int j = 0; j < N; ++j) {
            scanf("%d", &t);
            ++(height[t]);
        }
    }

    for(int i = 1; i < 2501; ++i) {
        if(height[i] % 2 == 1) {
            printf(" %d", i);
        }
    }
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
