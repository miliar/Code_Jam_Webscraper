#include<cstdio>
#include<list>

using namespace std;


// for qsort
/*
int compare(int *t, int *s) {
    return *t - *s;
}
*/

char S[1004];


void solve() {
    char front = S[0];
    list<char> p;
    p.push_front(front);
    for(int i = 1; S[i] != '\0'; ++i) {
        if(front > S[i]) {
            p.push_back(S[i]);
        }
        else {
            front = S[i];
            p.push_front(front);
        }
    }

    for(auto iter = p.begin(); iter != p.end(); ++iter) {
        putchar(*iter);
    }
}

void solve_and_print() {
    int i;

    gets(S);

    solve();
    printf("\n");
}


int main() {
    int dataset_num, case_num;

    scanf("%d", &dataset_num);
    gets(S);
    for(case_num = 1; case_num <= dataset_num; ++case_num) {
        printf("Case #%d: ", case_num);

        solve_and_print();
    }

    return 0;
}
