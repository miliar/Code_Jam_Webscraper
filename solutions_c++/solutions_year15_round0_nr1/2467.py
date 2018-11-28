//
// Created by Morteza on 2015-04-11.
//

#include <iostream>
#include <vector>

using namespace std;

#define toDigit(c) (c-'0')

int main(int argc, const char *argv[]) {

    ios_base::sync_with_stdio(false);

    int test_no;

    cin >> test_no;

    for (int i = 0; i < test_no; ++i) {

        int si_max;
        int answer_tmp = 0;
        int total_tmp = 0;
        string si_tmp;

        cin >> si_max;
        cin >> si_tmp;

        for (int j = 0; j <= si_max; ++j) {
            int single_si_tmp = toDigit(si_tmp[j]);
            if (single_si_tmp > 0 && j > total_tmp) {
                answer_tmp += j - total_tmp;
                total_tmp += j - total_tmp;
            }
            total_tmp += single_si_tmp;
        }
        cout << "Case #" << (i + 1) << ": " << answer_tmp << endl;
    }
    return 0;
}