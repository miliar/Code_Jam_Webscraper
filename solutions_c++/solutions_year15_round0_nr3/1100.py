#include <iostream>
#include <algorithm>
#include <string>
#include <vector>


using namespace std;


int translate(char ch) {
    switch (ch) {
        case 'i':
            return 2;
        case 'j':
            return 3;
        case 'k':
            return 4;
        default:
            return 0;
    }
}

int mult(int x, char ch) {
    int t = translate(ch);
    if (x == 1) return t;
    if (x == -1) return -t;
    if (t == x) return -1;
    if (abs(x) == abs(t)) return 1;
    int res;
    switch (abs(x)) {
        case 2:
            res = (t == 3) ? 4 : -3;
            break;
        case 3:
            res = (t == 4) ? 2 : -4;
            break;
        case 4:
            res = (t == 2) ? 3 : -2;
            break;
        default:
            res = 0;
            break;
    }
    if (x < 0) res *= -1;
    return res;
}



int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T, L;
    unsigned long X;
    scanf("%d", &T);
    
    for (int c = 1; c <= T; c++) {
        printf("Case #%d: ", c);
        scanf("%d%lu", &L, &X);
        char str[10010];
        scanf("%s", str);
        long long length = L * X;
        int r = 1;
        for (int i = 0; i < L; i++) {
            r = mult(r, str[i]); 
        }
        if (X % 2 == 0) {
            if (abs(r) == 1) {
                printf("NO\n");
                continue;
            }
            if (X % 4 == 0) {
                printf("NO\n");
                continue;
            } 
        } else {
            if (r != -1) {
                printf("NO\n");
                continue;
            } 
        }
        int index = 0;
        r = 1;
        while ((index < length) && (index < 10 * L) && (r != 2)) {
            int i = index % L;
            r = mult(r, str[i]);
            index++;  
        }
        r = 1;
        while ((index < length) && (index < 10 * L) && (r != 3)) {
            int i = index % L;
            r = mult(r, str[i]);
            index++;
        }
        string res = (r == 3) ? "YES" : "NO";
        printf("%s\n", res.c_str());
    }
    return 0;
}
