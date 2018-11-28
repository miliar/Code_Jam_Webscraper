// Copyright 2015 Thiago Barbato

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>

using namespace std;

int main(int argc, char const *argv[]) {
    int n;
    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; i++) {
        string wins = "RICHARD";
        int x, r, c;

        cin >> x;
        cin >> r;
        cin >> c;

        if (x >= 7) {}
        else if (x >= 4 && (r <= 2 || c <= 2)) {}
        else if (((r*c) > x && (r*c) % x == 0 && (r*c) != x) || (r*c == x) && x <= 2) wins = "GABRIEL";

        cout << "Case #" << i + 1 << ": " << wins << endl;
    }
}
