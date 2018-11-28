#include<cstdio>

using namespace std;


// for qsort
/*
int compare(int *t, int *s) {
    return *t - *s;
}
*/

int n;
int Z;
int W;
int U;
int X;
int G;
int F;
int V;
int R;
int O;
int N;


int num[10];
char buf[10];

void solve() {
    for(int i = 0; i < 10; ++i) {
        num[i] = 0;
    }

    num[0] = Z;
    R -= Z;
    O -= Z;

    num[2] = W;
    O -= W;

    num[4] = U;
    F -= U;
    O -= U;
    R -= U;

    num[6] = X;

    num[8] = G;

    num[5] = F;
    V -= F;

    num[7] = V;
    N -= V;

    num[3] = R;

    num[1] = O;
    N -= O;

    num[9] = N/2;

    for(int i = 0; i < 10; ++i) {
        for(int j = 0; j < num[i]; ++j) {
            printf("%d", i);
        }
    }
}

void solve_and_print() {
    int flag = 1;
    Z = W = U = X = G = F = V = R = O = N = 0;
    while(flag) {
        switch(getchar()) {
        case 'Z': Z++; break;
        case 'W': W++; break;
        case 'U': U++; break;
        case 'X': X++; break;
        case 'G': G++; break;
        case 'F': F++; break;
        case 'V': V++; break;
        case 'R': R++; break;
        case 'O': O++; break;
        case 'N': N++; break;
        case '\n':
        case '\r':
            flag = 0; break;
        default: break;
        }
    }
    solve();
    printf("\n");
}


int main() {
    int dataset_num, case_num;

    scanf("%d", &dataset_num);
    gets(buf);

    for(case_num = 1; case_num <= dataset_num; ++case_num) {
        printf("Case #%d: ", case_num);

        solve_and_print();
    }

    return 0;
}
