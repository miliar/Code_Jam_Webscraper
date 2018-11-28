#include <string>
#include <cstdio>
using namespace std;

bool isAllFound(int hash[]) {
    for(int i=0; i<10; i++)
        if(!hash[i]) return 0;
    return 1;
}

void markDigits(int hash[], int num) {
    string st = to_string(num);
    for(int i=0; i<st.size(); i++)
        hash[st[i]-'0'] = 1;
}

int countingSheep(int n) {
    int digits[10] = {0};
    for(int i=1, tmp; tmp > 0; i++) {
        tmp = n * i;
        markDigits(digits, tmp);
        if(isAllFound(digits))
            return tmp;
    }
    return -1;
}

int main() {
    int tc; scanf("%d", &tc);
    for(int i=1; i<=tc; i++) {
        int n; scanf("%d", &n);
        int ans = countingSheep(n);

        if(ans == -1) printf("Case #%d: INSOMNIA\n", i);
        else printf("Case #%d: %d\n", i, ans);
    }
}