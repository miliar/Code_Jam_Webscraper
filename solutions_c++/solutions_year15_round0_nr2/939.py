#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <limits.h>
#include <math.h>
using namespace std;

const int N = 1000+10;

int num[N];

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas = 1 ; cas <= T ; ++cas) {
        memset(num,0,sizeof(num));
        int n;
        scanf("%d",&n);
        for(int i = 0 ; i < n  ; ++i) {
            int x;
            scanf("%d",&x);
            ++num[x];
        }
        int top = N-1;
        while(!num[top])--top;
        int answer = top;
        for(int i = top ; i > 0 ; --i) {
            int wait = 0;
            for(int j = top ; j > i ; --j) {
                if(j%i==0)
                    wait += num[j]* (j/i-1);
                else
                    wait += num[j]* (j/i);
            }
            answer = min(answer, wait+i);
        }
        printf("Case #%d: %d\n", cas, answer);
    }
}
