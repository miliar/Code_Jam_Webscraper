#include <iostream>
#include <cstring>

struct AA {
    char str[500];
    int u, d;
    void read() {
        std::cin >> str;
    }
    void parse() {
        char tmp[500] = {};
        int len = strlen(str);
        int id = 0;
        tmp[id++] = str[0];
        for (int i = 1; i < len; i++) {
            if (tmp[id-1] != str[i]) {
                tmp[id++] = str[i];
            }
        }
        strcpy(str, tmp);
    }
    void calc() {
        u = 0; d = 0;
        int len = strlen(str);
        if (len == 1 && str[0] == '-')
            u += 1;
        for (int i = 1; i < len; i++) {
            if (str[i-1] == '-' && str[i] == '+') { // -+
                u += 1;
                str[i-1] = '+';
            } else if (str[i-1] == '+' && str[i] == '-'){ // +-
                d += 1;
                str[i] = '+';
            }
        }
    }
    int output() {
        return u*1+d*2;
    }
};
int main() {
    int T;
    char str[500];
    std::cin >> T;
    for (int t = 1; t <= T; t++) {
        AA a;
        a.read();
        a.parse();
        a.calc();
        std::cout << "Case #" << t << ": " << a.output() << std::endl;
    }
    return 0;
}
