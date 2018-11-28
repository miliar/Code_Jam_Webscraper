#include <array>
#include <vector>
#include <iostream>
#include <algorithm>

#define r(_c_) begin(_c_), end(_c_)

using namespace std;

uint32_t discard;

array<uint32_t, 4> parseRow () {
    uint32_t choosen;
    cin >> choosen;

    array<uint32_t, 4> row;
    for (uint32_t i = 1; i <= 4; ++i) {
        if (i == choosen) 
            {cin >> row[0] >> row[1] >> row[2] >> row[3];}
        else
            {cin >> discard >> discard >> discard >> discard;}
    }
    return row;
} 

void solve () {
    array<uint32_t, 4> row1, row2;
    vector<uint32_t> intersection;

    row1 = parseRow();
    row2 = parseRow();
    sort (r(row1));
    sort (r(row2));
    set_intersection (r(row1), r(row2), back_inserter(intersection));

    if (intersection.size() == 1)     { cout << intersection[0]; }
    else if (intersection.size() > 1) { cout << "Bad magician!"; }
    else                              { cout << "Volunteer cheated!"; }
}

int main () {
    size_t T; cin >> T;
    for (size_t i = 1; i <= T; ++i)
        { cout << "Case #" << i << ": "; solve(); cout << "\n"; }
}