#include <cstdio>
#include <cctype>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#ifdef DEBUG
    int __msg_cnt = 0;
    #define msg(x) cerr<<++__msg_cnt<<" "<<__FUNCTION__<<"("<<__LINE__<<"): "<<x<<endl;
#else
    #define msg(x)
#endif

template<typename T>
inline void maximize(T& a, const T b) {
    if (b > a) a = b;
}
template<typename T>
inline void minimize(T& a, const T b) {
    if (b < a) a = b;
}

int scan() {
    char ch;
    int seg = 0;
    while (!isdigit(ch = getchar()))
        seg |= (ch == '-');
    int x = ch - '0';
    while (isdigit(ch = getchar()))
        x = x * 10 + ch - '0';
    return x;
}

void get_val(int x, int* X) {
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j) {
            int z = scan();
            if (x == i)
                X[j] = z;
    }
}

void work() {
    int a = scan() - 1, A[4];
    get_val(a, A);
    int b = scan() - 1, B[4];
    get_val(b, B);
    int target = -1;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (A[i] == B[j]) {
                if (target == -1) {
                    target = A[i];
                    continue;
                }
                cout<< "Bad magician!";
                return;
    }
    if (target == -1) {
        cout<< "Volunteer cheated!";
        return;
    }
    cout<< target;
}

int main() {
    int z = scan();
    for (int i = 1; i <= z; ++i) {
        cout<< "Case #"<< i<< ": ";
        work();
        cout<< endl;
    }
}
