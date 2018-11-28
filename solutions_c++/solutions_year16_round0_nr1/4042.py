#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int T, N;
    scanf("%d", &T);

    for(int t = 1 ; t <= T ; t++) {
        scanf("%d", &N);

        if(N == 0) {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }

        vector<bool> named(10, false);
        int named_count = 0;

        for(int i = 1 ; i <= 1000 ; i++) {
            int num = N * i;
            vector<int> digits;
            while(num > 0) {
                digits.push_back(num % 10);
                num /= 10;
            }

            for(int x = 0 ; x < digits.size() ; x++) {
                if(named[digits[x]] == false) {
                    named[digits[x]] = true;
                    named_count++;
                }
            }

            if(named_count == 10) {
                printf("Case #%d: %d\n", t, N * i);
                break;
            }
        }

        if(named_count < 10)
           printf("Case #%d: INSOMNIA\n", t);
    }

    return 0;
}
