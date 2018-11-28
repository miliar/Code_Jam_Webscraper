#include <iostream>
using namespace std;

void getLine(int line[]) {
    int c, n; cin >> c;
    for (int i=1; i<=4; ++i)
        for (int j=0; j<4; ++j) {
            cin >> n;
            if (i==c) line[j] = n;
        }
}

int crossNum(int x[], int y[], int n, int &ans) {
    int cross = 0;
    for (int i=0; i<n; ++i)
        for (int j=0; j<n; ++j)
            if (x[i]==y[j]) ++cross, ans=x[i];
    return cross;
}

int main() {
    int N; cin >> N;
    for (int casei=1; casei<=N; ++casei) {
        int x[4], y[4];
        getLine(x);
        getLine(y);
        int ans;
        int cross = crossNum(x, y, 4, ans);
        if      (cross==1) cout << "Case #" << casei << ": " << ans << endl;
        else if (cross<1)  cout << "Case #" << casei << ": Volunteer cheated!" << endl;
        else               cout << "Case #" << casei << ": Bad magician!" << endl;
    }
    return 0;
}
