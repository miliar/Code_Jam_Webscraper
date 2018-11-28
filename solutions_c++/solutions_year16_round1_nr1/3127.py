#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define pf push_front

int main() {
    int tc, x = 1;
    for(scanf("%d", &tc); tc--; ) {
        deque<char> dq;
        char in[1002];
        scanf("%s", in);

        dq.pb(in[0]);
        for(int i=1; in[i]; i++) {
            if(in[i] >= dq.front())
                dq.pf(in[i]);
            else
                dq.pb(in[i]);
        }

        printf("Case #%d: ", x++);
        while(!dq.empty()) 
            printf("%c", dq.front()), dq.pop_front();
        printf("\n");
    }

    return 0;
}