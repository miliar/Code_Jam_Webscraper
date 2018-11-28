#include <iostream>

bool areAllSeen(bool* seen) {
    for (int i = 0; i < 10; ++i) {
        if (!seen[i]) {
            return false;
        }
    }
    return true;
}

void printSeen(bool* seen, int i) {
    std::cout << i << ':';
    for (int j = 0; j < 10; ++j) {
        if (seen[j]) {
            std::cout << ' ' << j;
        }
    }
    std::cout << std::endl;
}

void updateSeen(bool* seen, int x) {
    while (x > 0) {
        seen[x % 10] = true;
        x = x / 10;
    }
}

int main() {
    int T;
    std::cin >> T;
    int C = 1;
    while (C <= T) {
        int N;
        std::cin >> N;
        bool seen[10] = {false};
        int i;
        for (i = 1; !areAllSeen(seen); ++i) {
            updateSeen(seen, i * N);
            //printSeen(seen, i);
            if (areAllSeen(seen)) {
                break;
            }
            if (i > 1000) {
                break;
            }
        }
        if (areAllSeen(seen)) {
            std::cout << "Case #" << C << ": " << i * N << std::endl;
        } else {
            std::cout << "Case #" << C << ": INSOMNIA" << std::endl;
        }
        C++;
    }
    return 0;
}
