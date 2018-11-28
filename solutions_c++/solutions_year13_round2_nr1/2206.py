#pragma comment(linker,"/STACK:268435456")

#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <ctime>
#include <set>
#include <map>

using namespace std;

#define all(a) a.begin(), a.end()
#define PI 3.14159265358979
#define sz(a) (int)a.size()
#define ppb push_back
#define mp make_pair

template <class T> T sqr(T n) {
    return n*n;
}

template <class T> T gcd(T a, T b) {
    while (b) {
        a %= b;
        cout << a << " " << b << endl;
        swap(a, b);
    }
    return a;
}

const int SZ = 510;
const int INF = 1000*1000*1000;

double start, finish;
/****************************************************************************/
void startTimer() {
#ifdef _DEBUG
    start = clock();
#endif
}

void stopTimer() {
#ifdef _DEBUG
    finish = clock();
    cout << "\n*** Total time ***\n" << (finish - start)/CLOCKS_PER_SEC << endl;
#endif
}
/****************************************************************************/

vector <int> motes;
int tests, A, N, cnt = 0, t = 0;

void getData() {
    cin >> tests;
}

void upSum(int x) {
    while (1) {
        if (A > x) {
            A += x;
            return;
        }
        A += (A - 1);
        ++t;
        if (A == 1) {
            return;
        }
    }
}

void solve() {
    for (int i = 0; i < tests; ++i) {
        cin >> A >> N;
        motes.resize(N);
        for (int j = 0; j < N; ++j) {
            cin >> motes[j];
        }
        sort(all(motes));
        for (int j = 0; j < N; ++j) {
            if (A <= motes[j]) {
                upSum(motes[j]);
            } else {
                A += motes[j];
            }
            if (t > N - j) {
                t = N - j;
                cnt += t;
                break;
            }
            cnt += t;
            t = 0;
        }
        cout << "Case #" << i + 1 << ": " << cnt << endl;
        cnt = t = 0;
        motes.clear();
    }
}

int main() {

ios::sync_with_stdio(false);    
freopen("input.txt", "r", stdin);   
freopen("output.txt", "w", stdout);

startTimer();

    getData();
    solve();

stopTimer();
    return 0;
}