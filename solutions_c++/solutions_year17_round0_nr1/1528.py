#include <cstdio>
#include <cstring>
using namespace std;

int main() {

    int T;
    scanf("%d", &T);
    for(int NCASE=1; NCASE<=T; ++NCASE) {
        char S[1004];
        int K;
        scanf("%s%d", S, &K);
        int N = strlen(S);
        int cost = 0;
        for(int i=0; i<=N-K; ++i) {
            if( S[i] == '-' ) {
                for(int j=0; j<K; ++j)
                    S[i+j] = (S[i+j] == '+' ? '-' : '+');
                ++cost;
            }
        }
        bool ok = true;
        for(int i=0; i<N; ++i)
            if( S[i] != '+' )
                ok = false;
        printf("Case #%d: ", NCASE);
        if( ok ) printf("%d\n", cost);
        else puts("IMPOSSIBLE");
    }

    return 0;
}
