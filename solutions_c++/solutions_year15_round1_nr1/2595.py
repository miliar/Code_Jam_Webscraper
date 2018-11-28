// Compile with: clang++ -std=c++11 -stdlib=libc++ example.cpp

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <vector>
#include <string>

using namespace std;

int methodOne(int* arr, int len) {
    int min = 0;
    for (int i = len -1; i > 0; --i) {
        if (arr[i - 1] > arr[i]) {
            min += (arr[i - 1] - arr[i]);
        }
    }
    return min;
}

int methodTwo(int* arr, int len) {
    int rate = 0;
    for (int i = 0; i < len - 1; ++i) {
        int temp = arr[i] - arr[i + 1];
        if (arr[i + 1] < arr[i] && temp > rate) {
            rate = temp;
        }
    }
    int min = 0;
    for (int i = 0; i < (len - 1); ++i) {
        if (arr[i] < rate) {
            min += arr[i];
        }
        else {
            min += rate;
        }
    }
    return min;
}

int main() {
    int T = 0;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int num_shrooms = 0;
        cin >> num_shrooms;
        int shrooms[num_shrooms];
        for (int i = 0; i < num_shrooms; ++i) {
            cin >> shrooms[i];
        }
        cout << "Case #" << t <<": "<< methodOne(shrooms, num_shrooms) << " " << methodTwo(shrooms, num_shrooms) << endl;
    }
    return 0;
}

