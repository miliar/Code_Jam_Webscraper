#include <cstdio>
#include <cstring>

#define REP(i,a,b) for (int i = int(a); i < int(b); ++i)

using namespace std;

typedef unsigned long long ull;

int main() {
    int numCases, numCase = 1, cont;
    ull number, decompose, i;
    bool readed[10], pass;
    
    scanf("%d", &numCases);
    
    while (numCases--) {
        scanf("%llu", &number);
        
        if (number == 0) {
            printf("Case #%d: INSOMNIA\n", numCase++);
            continue;
        }
        
        cont = 1;
        memset(readed, false, sizeof readed);
        while (true) {
            decompose = number * cont++;
            while (decompose > 0) {
                i = decompose % 10;
                decompose /= 10;
                readed[i] = true;
            }
            pass = true;
            REP(i, 0, 10) {
                if (!readed[i]) {
                    pass = false;
                    break;
                }
            }
            if (pass) {
                break;
            }
        }
        printf("Case #%d: %llu\n", numCase++, (number * (cont - 1)));
    }
    
    return 0;
}
