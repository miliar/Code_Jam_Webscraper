#include "iostream"
#include "cstring"
#include "cstdio"
using namespace std;
const int N = 110;
int main(void)
{
    int T;
    scanf("%d", &T);
    int g = 0;
    while(T--){
        printf("Case #%d:", ++g);
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        for(int i = 1; i <= k; ++ i){
            long long pos = i;
            for (int j = 1; j < c; ++ j){
                pos = (pos - 1) * k + i;
            }
            printf(" %lld", pos);
        }
        printf("\n");
    }
    return 0;
}