#include <cstdio>
#include <iostream>
#include <string>

typedef long long int LLI;

using namespace std;

string tag(int i) {
    static char buf[10000];
    sprintf(buf, "Case #%d: ", i + 1);
    return string(buf);
}

bool check(int *buf) {
    for (int i = 0; i < 10; ++i) {
        if (buf[i] == 0) { return false; }
    }
    return true;
}
string solve(LLI n) {
    static char out[10000];
    
    if (n == 0) {
        return "INSOMNIA";
    } else {
        int i = 0;
        int buf[10];
        memset(buf, 0, sizeof(buf));
        do {
            i++;
            LLI x = i * n;
            while (x > 0) {
                buf[x % 10] = 1;
                x /= 10;
            }
        } while (!check(buf));
        
        sprintf(out, "%lld", i * n);
        return string(out);
    }
}

int main(int argc, char *argv[]) {
    int num;
    cin >> num;

    for (int i = 0; i < num; ++i) {
        LLI x;
        cin >> x;
        cout << tag(i) << solve(x) << endl;
    }
    return 0;
}
