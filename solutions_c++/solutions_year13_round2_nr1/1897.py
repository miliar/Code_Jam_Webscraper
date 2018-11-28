#include <cstdio>
#include <algorithm>

using namespace std;
int tests, A, N;
int motes[107];
int steps[107];

void calSteps() {
    long long size = A, r;
    for (int i = 0; i < N; i++) {
        r = 0;
        if (size > motes[i]) {
            //printf("La mota de tamano %d fue absorbida ahora pase de %lld a %lld\n", motes[i], size, size+motes[i]);
            size += motes[i];
        } else {
            while (size <= motes[i]) {
                //printf("La mota es de tamano %d\n", motes[i]);
                //printf("Tengo size %lld y aumento a %lld\n", size, size*2-1);
                size = size*2 - 1;
                r++;
            }
            size += motes[i];
        }
        steps[i] = r;
    }
    
}

main() {
    scanf("%d", &tests);
    for (int i = 1; i <= tests; i++) {
        scanf("%d %d", &A, &N);
        for (int j = 0; j < N; j++) {
            scanf("%d", &motes[j]);
            steps[j] = 0;
        }
        sort(motes, motes+N);
        
        long long r = 0, size = A, aux;
        if (size == 1) {
            r = N;
        } else {
            calSteps();
            for (int j = 0; j < N; j++) {
                if (r + steps[j] >=  r + (N - j)) {
                    r += (N - j);
                    break;
                } else {
                    r += steps[j];
                }
            }
        }
        if (r > N) r = N;
        printf("Case #%d: %lld\n", i, r);
    }
}
