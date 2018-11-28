#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

int main()
{
    int T;
    int test_case;
    int s_max;
    int count;
    int friends, tmp;
    string audience;

    cin >> T;
    test_case = 1;
    while (test_case <= T) {
        cin >> s_max;
        cin >> audience;

        count = 0;
        friends = 0;

        for (int i = 0; i < audience.size(); i++) {
            count += atoi(audience.substr(i, 1).c_str());

            if (count < (i+1)) {
                tmp = (i+1) - count;
                friends += tmp;
                count += tmp;
            }
        }

        cout << "Case #" << test_case << ": " << friends << endl;
        test_case++;
    }

    return 0;
}
