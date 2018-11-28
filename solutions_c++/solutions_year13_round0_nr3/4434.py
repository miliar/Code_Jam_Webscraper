#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;

bool is_palindrome(long long n)
{
    vector<int> v;
    vector<int>::iterator ibegin;
    vector<int>::iterator iend;

    while (n) {
        v.push_back(n % 10);
        n /= 10;
    }

    ibegin = v.begin();
    iend = ibegin + v.size() - 1;
    while (*ibegin == *iend) {
        ibegin++;
        iend--;
    }

    return ibegin >= iend;
}

int main(int argc, char *argv[])
{
    int T;

    ifstream ifs(argv[1]);
    ofstream ofs(argv[2]);

    ifs >> T;

    for (int i = 1; i <= T; i++) {
        long long min;
        long long max;
        long long count = 0;
        long long begin;
        long long end;

        ifs >> min >> max;

        begin = sqrtl(min);
        end = sqrtl(max);
        if (begin * begin < min) {
            begin++;
        }

        for (long long j = begin; j <= end; j++) {
            long long n = j * j;

            if (is_palindrome(n) && is_palindrome(j)) {
                count++;
            }
        }

        ofs<< "Case #" << i << ": " << count << endl;
    }

    ifs.close();
    ofs.close();
    return 0;
}
