#include <cstdio>
#include <cassert>

//#define DEBUG

#ifdef DEBUG
#define DBG(...) printf(__VA_ARGS__)
#else
#define DBG(...)
#endif

inline void GABO(int C) { printf("Case #%d: GABRIEL\n", C); }
inline void RISO(int C) { printf("Case #%d: RICHARD\n", C); }
using namespace std;

typedef long long ll;


int main() {

    int T, TC = 1;
    scanf("%d", &T);

    while (T--) {
        int X, R, C;
        scanf("%d%d%d", &X, &R, &C);
        DBG("%d%d%d", X, R, C);
        int S = R*C;
        if (S%X != 0 || X > S || (X > R && X > S)) RISO(TC); // nevopchame to tam
        else if (X == 1) GABO(TC);
        else if (X == 3) {
            if (R >= 2 && C >= 2) GABO(TC);
            else RISO(TC);
        }
        else if (X == 4) {
            if ((R==3 && C==4) || (R==4 && C==3) || (R == 4 && C == 4)) GABO(TC);
            else RISO(TC);
        }
        else if (X >= 7) RISO(TC);
        else GABO(TC);
        TC++;
    }
    return 0;
}

