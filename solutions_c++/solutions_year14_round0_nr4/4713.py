#include <cstdio>
#include <iostream>
using namespace std;

int solve(float k[], float n[], int N) {
    float a;
    int index = 0;
    int total = 0;
    for(int i = 0; i < N; i++) {
        a = k[i];
        while(n[index] < a && index < (N - 1)) {
            index++;
        }
        if(index < N && n[index] > a) {
            total++;
            index++;
        }
    }
    return total;
}

int main()
{
    int T;
    int N;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        scanf("%d", &N);
        float k[N];
        float n[N];
        for(int i = 0; i < N; i++) {
            cin >> n[i];
        }
        for(int i = 0; i < N; i++) {
            cin >> k[i];
        }
        sort(k, k + N, less<float>());
        sort(n, n + N, less<float>());
        printf("Case #%d: %d %d\n", t, solve(k, n, N), N - solve(n, k, N));
    }
}

