// mars.ma
#include <iostream>
#include <string>
#include <cassert>

using namespace std;

int main(void)
{
    int testcase;  cin >> testcase;
    for (int tc = 1; tc <= testcase; tc++) {
        int len;
        string s;
        cin >> len >> s;
        assert(0 == len+1-s.length());
        int result = 0;
        int sum = s[0]-'0';
        for (int i = 1, sZ = s.length(); (i < sZ) && (sum < len); ++i) {
            if (sum < i) {
                result += i-sum;
                sum += i-sum;
            }
            sum += s[i] - '0';
        }

        cout << "Case #" << tc << ": " << result << endl;
    }

    return 0;
}

