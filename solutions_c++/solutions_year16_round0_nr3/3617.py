//
// Created by 강경완 on 16. 4. 9..
//

#include <iostream>
#include <math.h>


using namespace std;

unsigned long long change(char ary[], int d) {
    int n = strlen(ary);
    unsigned long long result = 0;
    for (int i = 0; i < n; i++) {
        if (ary[i] == '1')
            result += pow(d,i);
    }
    return result;
}

void printdex(char ary[]){
    int i= strlen(ary);
    for(int j=i-1; j>=0; j--)
    {
        printf("%c",ary[j]);
    }
}

void todex(char ary[], int num) {
    for (int i = 0; num > 0; i++) {
        ary[i] = '0' + (num % 2);
        num = num / 2;
    }
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int N, J;
        scanf("%d %d", &N, &J);
        unsigned long long up, down;

        down = up = pow(2, N - 1) + 1;
        for (int g = 1; g < N; g++) {
            up += pow(2, g - 1);
        }
        printf("%d %d\n", up, down);
        printf("Case #%d:\n", i+1);
        for (int r = 0; r < J;down++) {
            char ttt[77] = {0,};
            todex(ttt, down);
            if(ttt[0] == '0'){
                printf("%d\n", down);
                continue;
            }

            if (down >= up) {
                printf("%d %d error", up, down);
                exit(0);
            }
            unsigned long long table[11] = {0,};
            bool flag = true;
            for (int j = 2; j <= 10; j++) {
                unsigned long long result = change(ttt, j);
                printf("result : %d\n", result);
                for (unsigned long long k = 2; k < result; k++) {
                    if (!(result % k)) {
                        table[j] = k;
                        break;
                    }
                }
                if (table[j] == 0) {
                    flag = false;
                    printf("%d\n", down);
                    break;
                }
            }
            if (flag == false)
                continue;
            else {
                todex(ttt, down);
                printdex(ttt);
                for (int v = 2; v <= 10; v++)
                    printf(" %d", table[v]);
                r++;
                printf("\n");
            }
        }
    }
}
