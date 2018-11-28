#include<iostream>
using namespace std;

int check(bool *digits, int num) {
    int x = 0;
    while(num)  {
        int r = num % 10;
        num /= 10;
        if(!digits[r]) {
            digits[r] = true;
            ++x;
        }
    }
    return x;
}

void run() {
    int n;
    cin >> n;
    if(!n) cout << "INSOMNIA";
    else {
        bool digits[10] = {false};
        int cnt = 0;
        int x = 0;
        while(cnt < 10) {
            x += n;
            cnt += check(digits, x);
        }
        cout << x;
    }
}

int main(int argc, char *argv[]) {
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        run();
        cout << endl;
    }
    return 0;
}
