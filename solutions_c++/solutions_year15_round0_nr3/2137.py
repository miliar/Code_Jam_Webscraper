#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
using namespace std;

int T;

char qmul(char a, char b) {
    switch (a) {
    case '1':
        return b;
    case 'A':
        switch (b) {
        case '1': return 'A';        case 'A': return '1';
        case 'i': return 'I';        case 'I': return 'i';
        case 'j': return 'J';        case 'J': return 'j';
        case 'k': return 'K';        case 'K': return 'k';
        }
    case 'i':
        switch (b) {
        case '1': return 'i';        case 'A': return 'I';
        case 'i': return 'A';        case 'I': return '1';
        case 'j': return 'k';        case 'J': return 'K';
        case 'k': return 'J';        case 'K': return 'j';
        }
    case 'I':
        switch (b) {
        case '1': return 'I';        case 'A': return 'i';
        case 'i': return '1';        case 'I': return 'A';
        case 'j': return 'K';        case 'J': return 'k';
        case 'k': return 'j';        case 'K': return 'J';
        }
    case 'j':
        switch (b) {
        case '1': return 'j';        case 'A': return 'J';
        case 'i': return 'K';        case 'I': return 'k';
        case 'j': return 'A';        case 'J': return '1';
        case 'k': return 'i';        case 'K': return 'I';
        }
    case 'J':
        switch (b) {
        case '1': return 'J';        case 'A': return 'j';
        case 'i': return 'k';        case 'I': return 'K';
        case 'j': return '1';        case 'J': return 'A';
        case 'k': return 'I';        case 'K': return 'i';
        }
    case 'k':
        switch (b) {
        case '1': return 'k';        case 'A': return 'K';
        case 'i': return 'j';        case 'I': return 'J';
        case 'j': return 'I';        case 'J': return 'i';
        case 'k': return 'A';        case 'K': return '1';
        }
    case 'K':
        switch (b) {
        case '1': return 'K';        case 'A': return 'k';
        case 'i': return 'J';        case 'I': return 'j';
        case 'j': return 'i';        case 'J': return 'I';
        case 'k': return '1';        case 'K': return 'A';
        }
    }
    return 'X';
}

map<const char*, map<const char*, bool> > cache2;

bool canDo(const char* str, const char* s) {
    if (*str == 0 && *s == 0) return true;
    if (*str == 0 || *s == 0) return false;
    map<const char*, bool>& cache1 = cache2[s];
    map<const char*, bool>::iterator it = cache1.find(str);
    if (it != cache1.end()) return it->second;

    int len = 1;
    char res = str[0];
    while (true) {
        while (res != s[0]) {
            if (str[len] == 0) return (cache1[str] = false);
            res = qmul(res, str[len]);
            len++;
        }
        if (canDo(str + len, s + 1)) return (cache1[str] = true);
        if (str[len] == 0) return (cache1[str] = false);
        res = qmul(res, str[len]);
        len++;
    }
    return (cache1[str] = false);
}

bool solve() {
    cache2.clear();
    int L, X;
    cin >> L >> X;
    char sub[20000];
    string ss;
    for (int i = 0; i < L; ++i) {
        do { cin.read(&sub[i], 1); } while (!isalpha(sub[i]));
    }
    string s(sub, sub + L);
    for (int j = 0; j < X; ++j) {
        ss += s;
    }
    return canDo(ss.c_str(), "ijk");
}

int main(int argc, char* argv[]) {
#if 0
    char a[] = {'1','i','j','k','A','I','J','K'};
    for (int i = 0; i < 8; ++i) {
    for (int j = 0; j < 8; ++j) {
        switch (qmul(a[i], a[j])) {
            case 'A': printf("-1 "); break;
            case 'I': printf("-i "); break;
            case 'J': printf("-j "); break;
            case 'K': printf("-k "); break;
            default: printf(" %c ", qmul(a[i], a[j])); break;
        }
        
    }
    printf("\n");
    }
    return 0;
#endif

    cin >> T;
    for (int t = 0; t != T; ++t) {
        if (solve())
            printf("Case #%d: YES\n", t + 1);
        else
            printf("Case #%d: NO\n", t + 1);
    }
    return 0;
}

