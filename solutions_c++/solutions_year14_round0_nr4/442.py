#include <iostream>
#include <vector>
#include <iomanip>
#include <set>

using namespace std;

int T, N;

set<double> setX, setY;

bool isTrivial() {
    return *(setX.begin()) > *(--setY.end());
}

int getResult() {
    if (isTrivial()) {
        return N;
    }

    int result = 0;
    set<double> X = setX, Y = setY;

    double xVal;
    while (!X.empty()) {
        xVal = *(X.begin());
        auto yIter = Y.upper_bound(xVal);
        if (yIter == Y.end()) {
            ++result;
            Y.erase(Y.begin());
        }
        else {
            Y.erase(yIter);
        }
        X.erase(X.begin());
    }

    return result;
}

bool canCheat() {
    if (isTrivial()) {
        return true;
    }

    auto x = setX.begin();
    auto y = setY.begin();
    while (x != setX.end()) {
        if (*x < *y) {
            return false;
        }
        ++x; ++y;
    }

    return true;
}

void solve() {
    double win;
    int resultNoCheating = 0;

    setX.clear();
    setY.clear();

    for (int i = 0; i < N; ++i) {
        cin >> win;
        setX.insert(win);
    }

    for (int i = 0; i < N; ++i) {
        cin >> win;
        setY.insert(win);
    }

    resultNoCheating = getResult();
    while (N > 0 && !canCheat()) {
        setX.erase(setX.begin());
        setY.erase(--setY.end());
        --N;
    }

    cout << N << " " << resultNoCheating << "\n";
}

int main() {
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        cin >> N;
        solve();
    }
}

