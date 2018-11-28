#include <iostream>
#include <map>
#include <cstring>

using namespace std;

bool fallAsleep(int D[]);

void doCase(int iCase) {
    printf("Case #%d: ", iCase);

    int N; scanf("%d", &N);
    int D[10]; memset(D, 0, sizeof(D));
    map<int, bool> M; M.clear();
    
    int n = N;
    while (M[n] == false && !fallAsleep(D)) {
        M[n] = true;
        
        int t = n;
        while (t > 0) {
            D[t % 10] = 1;
            t /= 10;
        }

        if (fallAsleep(D)) break;
        
        n += N;
    }
    
    if (!fallAsleep(D)) puts("INSOMNIA");
    else printf("%d\n", n);
}

bool fallAsleep(int D[]) {
    for (int i=0; i<=9; i++) {
        if (D[i] == 0) return false;
    }
    return true;
}

int main(void) {
    int T; scanf("%d", &T);
    for (int i=1; i<=T; i++) doCase(i);
	return 0;
}