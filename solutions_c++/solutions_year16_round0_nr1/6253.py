/*
 * SORTING
 *
 * Ex. 1
 * sort(intVec.begin(), intVec.end());
 *
 * Ex. 2
 * bool wayToSort(int i, int j) { return i > j; }
 * sort(intVec.begin(), intVec.end(), wayToSort);
 *
 * Ex. 3
 * sort(intArray, intArray + SIZE);
 */

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <vector>
#include <string>

using namespace std;

#define ULLI unsigned long long int
#define TRACK_SIZE 10

void init_track(bool* track) {
    for (int i = 0; i < TRACK_SIZE; ++i) {
        track[i] = false;
    }
}

void update_track(ULLI N, bool* track) {
    do {
        int modulo = N % 10;
        N /= 10;
        track[modulo] = true;
    } while (N != 0);
}

bool is_track_complete(bool* track) {
    for (int i = 0; i < TRACK_SIZE; ++i) {
        if (track[i] == false) return false;
    }
    return true;
}

ULLI manually_count_sheep(ULLI N) {
    bool track[TRACK_SIZE];
    init_track(track);
    update_track(N, track);

    ULLI i = 2;
    ULLI M = N;
    while (!is_track_complete(track)) {
        M = i * N;
        update_track(M, track);
        ++i;
    }

    return M;
}

int main() {
    int T = 0;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        ULLI N = 0;
        cin >> N;

        if (N == 0) {
            cout << "Case #" << t <<": INSOMNIA" << endl;
        }
        else {
            cout << "Case #" << t <<": "<< manually_count_sheep(N) << endl;
        }
    }
    return 0;
}
