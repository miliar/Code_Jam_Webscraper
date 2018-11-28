#include <cstdio>
#include <string>
using namespace std;

int main() {
    int T; scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        int N; scanf("%d", &N);
        if (N == 0) {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }
        
        int n = N;
        
        string s = "..........";
        while (true) {
            char buf[100];
            sprintf(buf, "%d", n);
            for (int i=0; buf[i]; i++)
                s[buf[i]-'0'] = 'x';
            if (s == "xxxxxxxxxx")
                break;
            n += N;
        }
        
        printf("Case #%d: %d\n", t, n);
    }
    return 0;
}
