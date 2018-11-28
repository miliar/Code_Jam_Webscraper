#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {

    int T;

    scanf("%d", &T);

    for (int ts = 0; ts < T; ts++) {

        int N;
        char arr[1010];

        scanf("%d %s", &N, arr);

        int s = 0, r = 0;
        
        for (int j = 0; arr[j]; j++) {

            if (arr[j] != '0') {
                s += max(j-r, 0);
                r += max(j-r, 0);
            }

            r += arr[j]-'0';
        }

        printf("Case #%d: %d\n", ts+1, s);
    }
}
