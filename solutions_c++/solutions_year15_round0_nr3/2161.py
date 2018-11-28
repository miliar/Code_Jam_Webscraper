#include <iostream>

using namespace std;

int calc(char &now, char x) {
    if (now == '1') {
        now = x;
        return 1;
    }
    if (x == '1') {
        return 1;
    }
    if (now == 'i') {
        if (x == 'i') {
            now = '1';
            return -1;
        }
        if (x == 'j') {
            now = 'k';
            return 1;
        }
        if (x == 'k') {
            now = 'j';
            return -1;
        }
    }
    if (now == 'j') {
        if (x == 'i') {
            now = 'k';
            return -1;
        }
        if (x == 'j') {
            now = '1';
            return -1;
        }
        if (x == 'k') {
            now = 'i';
            return 1;
        }
    }
    if (now == 'k') {
        if (x == 'i') {
            now = 'j';
            return 1;
        }
        if (x == 'j') {
            now = 'i';
            return -1;
        }
        if (x == 'k') {
            now = '1';
            return -1;
        }
    }
    return 1;
}

void solve(int t) {
    int X;
    int L, i, j, sign = 1;
    int flag = 0;
    char now = '1';
    char c[10010];
    cin>>L>>X;
    for (i = 0; i < L; i++) {
        cin>>c[i];
    }
    for (j = 0; j < X; j++) {
        for (i = 0; i < L; i++) {
            sign = sign * calc(now, c[i]);
            if (flag == 0) {
                if ((now == 'i') && (sign == 1)) {
                    flag++;
                }
            } else if (flag == 1) {
                if ((now == 'k') && (sign == 1)) {
                    flag++;
                }
            }
        }
    }
    if ( (flag == 2) && (now == '1') && (sign == -1) ) {
        cout<<"Case #"<<t<<": YES"<<endl;
    } else {
        cout<<"Case #"<<t<<": NO"<<endl;
    }
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int t, i;
    cin>>t;
    for (i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
