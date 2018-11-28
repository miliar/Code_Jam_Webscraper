#include <iostream>
#include <cmath>

using namespace std;

int minutes(int d, int* ps) {
    int maxM = 0;
    for(int i = 0; i < d; i++) {
        if(ps[i] > maxM)
            maxM = ps[i];
    }
    int minMinutes = maxM;
    for(int m = 1; m < maxM; m++) {
        int mins = m - d;
        for(int i = 0; i < d; i++) {
            mins += ceil(ps[i]*1.0/m);
        }
        if(mins < minMinutes) {
            minMinutes = mins;
        }
    }
    return minMinutes;
}

int main() {
    int t;
    cin >> t;
    
    for(int i = 1; i <= t; i++) {
        int d;
        cin >> d;

        int* ps = new int[d];
        for(int j=0; j<d; j++) {
            cin >> ps[j];
        }
        
        cout << "Case #" << i << ": ";
        cout << minutes(d, ps);
        cout << endl;
    }

    return 0;
}

