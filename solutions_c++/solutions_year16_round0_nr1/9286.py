
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <cstdint>
#include <string>

using namespace std;


void update(uint64_t n, int m[], int& toFill) {
    while (n > 0) {
        int digit = n%10;
        if (!m[digit]) {
            m[digit] = 1;
            toFill--;
        }
        n /= 10;
    }
}

uint64_t solve(uint64_t n) {
    if (n == 0) return numeric_limits<uint64_t>::max();
    
    int map[10];
    int toFill = 10;
    memset(map, 0, sizeof(map));
    
    uint64_t r = 0;
    do {
        r += n;
        update(r, map, toFill);
    } while (toFill > 0);
        
    return r;
}

int main() {
    
    
	int tCases;
    cin >> tCases;
	for (int c = 1; c <= tCases; c++) {
        uint64_t num;
		cin >> num;

		uint64_t s = solve(num);

		cout << "Case #" << c << ": ";
		if (s == numeric_limits<uint64_t>::max()) {
			cout << "INSOMNIA\n";
		} else {
			cout << s << "\n";
		}
	}
}
