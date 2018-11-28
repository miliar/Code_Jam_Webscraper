#include <stdio.h>

using namespace std;

#define MAX_N 100000
int N, B;
int M[MAX_N+1];
int T[MAX_N+1];

int gcd(int a, int b){
    int x;
    while(b){
        x = a % b;
        a = b;
        b = x;
    }
    return a;
}

int lcd(int a, int b){
    int m = gcd(a, b);
    return a * (b / m);
}

int getBarber(){
    int num = -1;
    int min =100000 + 1;
    for (int i = 0; i < B; i++){
        if (T[i] == 0){
            num = i;
            break;
        }
        if (T[i] < min){
            min = T[i];
        }
    }
    if (num != -1){
        T[num] = M[num];
        return num;
    }
    for (int i = B - 1; i >= 0; i--){
        T[i] -= min;
        if (T[i] == 0) num = i;
    }
    T[num] = M[num];
    return num;
}

int solve(){
    for (int i = 0; i < B; i++){
        T[i] = 0;
    }

    int curr = M[0];
    for (int i = 1; i < B; i++){
        curr = lcd(curr, M[i]);
    }
    int skip = 0;
    for (int i = 0; i < B; i++){
        skip += curr / M[i];
    }

    int real = N % skip;
    if (real == 0) real = skip;

    int num = 0;
    for (int i = 0; i < real; i++){
        num = getBarber();
    }
    return num+1;
}


int main()
{
    int T;
    freopen("input.txt", "r", stdin);
    freopen("answer.txt", "w", stdout);
    setbuf(stdout, NULL);
    scanf("%d", &T);
    for (int i = 1; i <= T; i++){
        scanf("%d %d", &B, &N);
        for (int j = 0; j < B; j++){
            scanf("%d", &M[j]);
        }
        printf("Case #%d: %d\n", i, solve());
    }
}
