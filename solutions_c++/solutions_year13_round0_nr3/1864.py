#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <climits>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;

const ull maximo = 10000000;
vector<ull> fas_vector;

ull rev_num(ull n) {
    ull rev = 0;

    while (n > 0) {
        rev = rev*10 + (n%10);
        n /= 10;
    }

    return rev;
}

bool is_fair(ull n) {
    return n == rev_num(n);
}

void initialize() {
    ull square;
    for (ull i = 1; i <= maximo; i++) {
        square = i*i;
        if (is_fair(i) and is_fair(square)) fas_vector.push_back(square);
    }
}

ull magia(ull a, ull b) {
    vector<ull>::iterator beg, end;

    beg = lower_bound(fas_vector.begin(), fas_vector.end(), a);
    end = lower_bound(fas_vector.begin(), fas_vector.end(), b);

    if (beg == fas_vector.end()) return 0;

    if (end != fas_vector.end()) {
        if (*end != b) {
            return (end - beg);
        }
        else {
            return (1 + (end - beg));
        }
    }
    else {
        return (end - beg);
    }
}

int main () {
    ull t;
    ull a, b;

    initialize();

    cin >> t;
    for (ull i = 1; i <= t; i++) {
        cin >> a >> b;

        cout << "Case #" << i << ": " << magia(a, b) << endl;
    }

    return 0;
}
