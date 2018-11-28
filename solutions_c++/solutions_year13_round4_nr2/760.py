#include <iostream>

#define ll long long int

using namespace std;

int T;
int N;
ll P;

ll m;

int paras(int k) {
    int hu = m-(k+1);
    int v = 0;
    for (int i = 0; i < N; i++) {
        if (hu > 0) {
            v = v*2+1;
        } else {
            v = v*2;
        }
        if (hu%2 == 0) hu--;
        hu /= 2;
    }
    return (m-v);
}

int huonoin(int k) {
    int hu = k;
    int v = 0;
    for (int i = 0; i < N; i++) {
        if (hu > 0) {
            v = v*2;
        } else {
            v = v*2+1;
        }
        if (hu%2 == 0) hu--;
        hu /= 2;
    }
    return (m-v);
}

void laske(int n) {
    cin >> N >> P;
    m = 1<<N;
    cout << "Case #" << n << ": ";
    for (int i = m-1; i >= 0; i--) {
        if (huonoin(i) <= P) {
            cout << i << " ";
            break;
        }
    }
    for (int i = m-1; i >= 0; i--) {
        if (paras(i) <= P) {
            cout << i << endl;
            break;
        }
    }
}

int main() {
    cin >> T;
    for (int i = 0; i < T; i++) {
        laske(i+1);
    }
}