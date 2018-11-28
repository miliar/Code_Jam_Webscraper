#include <stdio.h>

using namespace std;

#define MAX_N 10000
int L;
long long X;
char str[MAX_N+1];
int val[MAX_N+1];
bool isMinus;

int mul[4][4] = {
    {0, 1, 2, 3},
    {1, 0, 3, 2},
    {2, 3, 0, 1},
    {3, 2, 1, 0},
};

int minus[4][4] = {
    {0, 0, 0, 0},
    {0, 1, 0, 1},
    {0, 1, 1, 0},
    {0, 0, 1, 1},
};

bool solve(){

    for (int i = 0; i < L; i++){
        val[i] = str[i] - 'i' + 1; // i : 1, j : 2, k : 3
    }

    int curr = 0;
    int count = 0;
    for (int i = 0; i < L; i++){
        count += minus[curr][val[i]];
        curr = mul[curr][val[i]];
    }
    isMinus = ((count & 1) == 1);

    // x번 반복
    if (isMinus == false || (X & 1) == 0){
        isMinus = false;
    }
    else {
        isMinus = true;
    }
    // x번 반복시 내용
    bool interMinus = false;
    if (curr != 0){
        curr = ((X & 1) == 0) ? 0 : curr;
        interMinus = ((X >> 1 & 1) == 1);
    }

    isMinus = (isMinus == interMinus) ? false : true;
    if (isMinus == false || curr != 0) return false;

    long long SI, EI;
    int sj, ej;
    bool isFindI = false;
    bool isFindK = false;
    curr = 0;
    count = 0;
    for (SI = 0; SI < X; SI++){
        for (sj = 0; sj < L; sj++){
            count += minus[curr][val[sj]];
            curr = mul[curr][val[sj]];
            if (curr == 1 && (count & 1) == 0){
                isFindI = true;
                break;
            }
        }
        if (isFindI == true) break;
    }

    curr = 0;
    count = 0;
    for (EI = X - 1; EI >= 0; EI--){
        for (ej = L - 1; ej >= 0; ej--){
            count += minus[val[ej]][curr];
            curr = mul[val[ej]][curr];
            if (curr == 3 && (count & 1) == 0){
                isFindK = true;
                break;
            }
        }
        if (isFindK == true) break;
    }
    if (EI < SI || (SI == EI && ej < sj)){
            return false;
    }
    return (isFindI == true) && (isFindK == true);
}

int main()
{
    int T;
    freopen("input.txt", "r", stdin);
    freopen("answer.txt", "w", stdout);
    setbuf(stdout, NULL);
    scanf("%d", &T);
    for (int i = 1; i <= T; i++){
        scanf("%d %I64d", &L, &X);
        scanf("%s", str);
        printf("Case #%d: %s\n", i, solve() ? "YES" : "NO");
    }
}
