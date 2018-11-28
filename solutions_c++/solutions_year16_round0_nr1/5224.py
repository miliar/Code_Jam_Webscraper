#include <iostream>

using namespace std;

int small (int n) {
    int m, x, i, cnt;
    bool w[10] = {false};
    i = n;
    cnt = 0;
    while (cnt < 10 && n != 0) {
        m = i;
        while (m > 0) {
            x = m % 10;
            m /= 10;
            if (!w[x]) ++cnt;
            w[x] = true;
        }
        i += n;
    }
    return i-n;
}

int main(){
    int tmax, n, m;
    cin >> tmax;
    for (int t=1; t<=tmax; ++t) {
        cin >> n;
        m = small(n);
        if (m == 0) {
            cout << "Case #" << t << ": INSOMNIA" << endl;
        } else {
            cout << "Case #" << t << ": " << m << endl;
        }

    }
    return 0;
}
