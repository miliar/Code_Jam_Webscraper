#include <cstdio>
#include <cstring>
using namespace std;

bool palindrome(int n) {
    char buf[100];
    sprintf(buf, "%d", n);
    int l = strlen(buf);
    for (int i=0; i<l/2; i++)
        if (buf[i]!=buf[l-1-i])
            return false;
    return true;
}


int main() {
    int T; scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        int A, B; scanf("%d%d", &A, &B);
        int cnt=0;
        for (int i=1; i<=33; i++) {
            int n=i*i;
            if (A<=n && n<=B && palindrome(i) && palindrome(n))
                cnt++;
        }
        printf("Case #%d: %d\n", t, cnt);
    }
    return 0;
}

