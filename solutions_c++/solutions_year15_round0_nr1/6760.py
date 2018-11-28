#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
    int T, Smax;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        scanf("%d", &Smax);
        int audience[Smax+1];
        char c= '0';
        int i = 0;
        while(i < Smax + 1) {
            c = getchar();
            if(c != ' ') {
                char array[2];
                array[0] = c;
                array[1] = '\0';
                audience[i] = atoi(array);
                i++;
            }
        }
        int res = 0;
        int count = audience[0];
        for(i = 1; i <= Smax; i++) {
            if(i > count + audience[i-1]) {
                res += i - count - audience[i-1];
                count += i - count  - audience[i-1];
            }
            count += audience[i];
        }
        printf("Case #%d: %d\n", t, res);
    }
}