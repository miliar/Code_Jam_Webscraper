#include <iostream>
#include <string>

using namespace std;

int main() {
    int t = 0 ,T;
    scanf("%d",&T);
    cin.ignore();
    while (t++ < T) {
        string str;
        char c = 0;
        unsigned long long count = 0, f = 0;
        bool isH = false, first = false;
        getline(cin, str, '\n');
        for (int i = 0; i < str.length(); ++i) {
            c = str[i];
            if (c == '\n') break;
            if (c == '-') {
                if (!isH) { if (first) count++; else f = 1; isH = true; }
            } else if (c == '+') {
                isH = false;
                first = true;
            }
        }
        printf("Case #%d: %lld\n", t, count*2+f);
    }
}