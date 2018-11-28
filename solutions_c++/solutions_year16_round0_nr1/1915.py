#include <iostream>

bool checkifallpresent(int Hash[], long int number) {
    while (number != 0) {
        Hash[number % 10] = 1;
        number = number / 10;
    }

    bool isPresent = true;
    for (int i = 0; i < 10; i++) {
        if (Hash[i] == 0) {
            isPresent = false;
            break;
        }
    }

    return isPresent;
}

int main(int argc, char** argv) {
    int times;
    std::cin >> times;

    for (int i = 0; i < times; i++) {
        long int N, runningN;
        std::cin >> N;
        runningN = N;
        int digitsHash[10];
        for (int k = 0; k < 10; k++) {
            digitsHash[k] = 0;
        }

        if (runningN == 0) {
            std::cout << "Case #" << i + 1 << ": " << "INSOMNIA" << std::endl;
            continue;
        }

        while (!checkifallpresent(digitsHash, runningN)) {
            runningN+=N;
        }
        std::cout << "Case #" << i + 1 << ": " << runningN << std::endl;
    }

    return 0;
}
