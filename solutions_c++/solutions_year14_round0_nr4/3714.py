#include<iostream>
#include<vector>
#include<math.h>
using namespace std;

int sortInverse(double i, double j) {
    return i > j;
}

int deceitfulWar(vector<double> w1, vector<double> w2, int n) {
    sort(w1.begin(), w1.end());
    sort(w2.begin(), w2.end());

    // for (int i = 0; i < n; i++) {
    //     cout << w1[i] << " ";
    // }
    // cout << endl;
    // for (int i = 0; i < n; i++) {
    //     cout << w2[i] << " ";
    // }
    // cout << endl;

    int score = 0;
    int i = 0, j = 0;
    while (i < n && j < n) {
        if (w1[i] < w2[j]) {
            i++;
            // lose; deceive w2 to use maximum available
        } else {
            score++;
            i++;
            j++;
        }
    }
    
    return score;
}

int war(vector<double> w1, vector<double> w2, int n) {
    sort(w1.begin(), w1.end(), sortInverse);
    sort(w2.begin(), w2.end(), sortInverse);

    // for (int i = 0; i < n; i++) {
    //     cout << w1[i] << " ";
    // }
    // cout << endl;
    // for (int i = 0; i < n; i++) {
    //     cout << w2[i] << " ";
    // }
    // cout << endl;


    int score = 0;
    int i = 0, j = 0;
    while (i < n && j < n) {
        if (w1[i] > w2[j]) {
            score++;
            i++;
        } else {
            i++;
            j++;
        }
    }
    
    return score;
}

int main() {
    int cases;
    cin >> cases;
    for (int c = 1; c <= cases; c++) {
        int n;
        cin >> n;
        vector<double> w1(n, 0);
        vector<double> w2(n, 0);
        for (int i = 0; i < n; i++) {
            cin >> w1[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> w2[i];
        }
        printf("Case #%d: %d %d\n", c, deceitfulWar(w1, w2, n), war(w1, w2, n));
    }
}
