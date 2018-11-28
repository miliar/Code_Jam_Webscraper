#include <iostream>
#include <limits>
#include <cmath>
#include <set>
#define whatIs(x) std::cerr << #x << ": " << x << std::endl;


using namespace std;

void digitToArray(long long*, long long, long long);

int main() {
    int t;
    std::cin >> t;
    for (int x = 1; x <= t; ++x) {
        long long n;
        std::cin >> n;

        std::set<long long> sett;
        bool keepOn = true;
        bool inSomnia = false;
        long long res;

        for (auto i = 1; keepOn; ++i) {
            if (n == 0) {
                inSomnia = true;
                std::cout << "Case #" << x <<": INSOMNIA" << std::endl;
                break;
            }
            long long num = n * i;
            const long long length = (long long)floor(log10((float)num)) + 1;
            long long a[length];
            digitToArray(a, num, length);

            for (auto i : a) {
                if (sett.insert(i).second) {
                    sett.insert(i);
                    if (std::distance(sett.begin(), sett.end()) == 10) {
                        keepOn = false;
                        break;
                    }
                }

            }
            res = num;
        }   // keepOn

        if (!inSomnia)
            std::cout << "Case #" << x << ": " << res << std::endl;

    }   // t

}

void digitToArray(long long* a, long long num, long long length) {
     do {
    	*a = num % 10;
    	num /= 10;
    	a++;
    } while (num != 0);

}


