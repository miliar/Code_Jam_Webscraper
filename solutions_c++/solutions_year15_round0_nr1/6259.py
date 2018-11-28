#include <cstdio>
#include <cassert>
#include <algorithm>

// #define DEBUG

#ifdef DEBUG
#define DBG(...) printf(__VA_ARGS__)
#else
#define DBG(...)
#endif

using namespace std;

typedef long long ll;


int main() {
    
    int T, C = 1;
    scanf("%d\n", &T);

    while (T--) {
        int maxi;
        scanf("%d ", &maxi);
        int i, needed, // kolko ludi treba pre postavenie sa tohto levelu
          total = 0, // celkovy pocet potrebnych priatelov 
          present = 0; // kolko zatial ludi stoji
        
        for (i=0; i<=maxi; i++) {
            int x = fgetc(stdin) - '0';
            if (x != 0) {
                needed = max(i-present, 0);
                DBG("i=%d needed=%d\n", i, needed);
                total += needed;
                present += needed+x;
            }
        }

        // doplnit nuly
        char buf;
        while ((buf = fgetc(stdin)) != '\n') ;

        printf("Case #%d: %d\n", C, total);
        C++;
    }
    return 0;
}

