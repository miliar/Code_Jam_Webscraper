#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int min(int a, int b) {
    if (a < b) {
        return a;
    } else {
        return b;
    }
}

int main() {
    int t;
    cin >> t;

    for (int i=1; i<=t; i++) {
        int nsamples;
        int shrooms1 = 0;
        int shrooms2_rate = 0;
        int shrooms2 = 0;
        cin >> nsamples;

        int samples[1000];
        cin >> samples[0];
        for (int j=1; j<nsamples; j++) {
            cin >> samples[j];
            if (samples[j] < samples[j-1]) {
                shrooms1 += samples[j-1] - samples[j];
                if (shrooms2_rate < samples[j-1] - samples[j]) {
                    shrooms2_rate = samples[j-1] - samples[j];
                }
            }
        }
        for (int j=1; j<nsamples; j++) {
            shrooms2 += min(samples[j-1], shrooms2_rate);
        }
        cout << "Case #" << i << ": " << shrooms1 << " " << shrooms2 << endl;
    }
    return 0;
}
