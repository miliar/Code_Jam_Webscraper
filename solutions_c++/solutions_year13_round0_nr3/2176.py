#include <iostream>
#include <string>

using namespace std;

bool isPalindrome(int X) {
    char str[128];
    sprintf(str, "%d", X);
    int len = strlen(str);
    for (int i = 0; i != len; ++i) {
        if (str[i] != str[len - 1 - i])
            return false;
    }
    return true;
}

int main(int argc, char* argv[])
{
    int T, A, B;
    cin >> T;
    for (int t = 0; t != T; ++t) {
        int cnt = 0;
        cin >> A >> B;
        for (int i = 1; i <= 1000; ++i) {
            int ii = i * i;
            if (ii >= A && ii <= B &&
                    isPalindrome(i) &&
                    isPalindrome(ii)) {
                ++cnt;
            }
        }
        cout << "Case #" << (t + 1) << ": " << cnt << "\n";
    }
    return 0;
}

