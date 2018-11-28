#include <iostream>
#include <string>

using namespace std;

bool allDigits(int digit[10]) {
    for (int i = 0; i < 10; i++) {
        if (digit[i] == 0) return false;
    }
    return true;
}

string lastN(const int n) {
    if (n == 0) return "INSOMNIA";
    int digit[10] = {};
    int count = n;
    do {
        int temp = count;
        while (temp > 0) {
            digit[temp % 10] = 1;
            temp /= 10;
        }
        if (allDigits(digit)) return to_string(count);
        count += n;
    } while (1);
}

int main(int argc, char const *argv[])
{
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int N;
        cin >> N;
        cout << "Case #" << i+1 << ": " << lastN(N) << endl;
    }
    return 0;
}
