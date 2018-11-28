#include <iostream>
#include <cstdio>

using namespace std;

bool isAll(bool t[10]) {
    for (int i = 0; i < 10; ++i) {
        if (!t[i]) {
            return false;
        }
    }
    return true;
}

void set(bool t[10], int s) {
    while (s > 0) {
        t[s%10] = true;
        s /= 10;
    }
}

int solve(int x) {
    if (x==0) return -1;

   bool t[10] = {0}; 
   int s = 0;
   while (!isAll(t)) {
       s += x;
       set(t, s);
   }
   return s;
}

int main() {
    int caseCnt = 0;
    cin >> caseCnt;
    for (int i = 0; i < caseCnt; ++i) {
        int s = 0;
        cin >> s;
        if (s == 0) {
            printf("Case #%d: INSOMNIA\n", i + 1);
        } else {
            int ans = solve(s);
            printf("Case #%d: %d\n", i + 1, ans);
        }
    }

    return 0;
}
