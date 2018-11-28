#include <iostream>
#include <fstream>

using namespace std;

int main(void) {
    int t, x;
    int tracker[20];
//    ifstream in ("A-small-attempt1.in", ios::in);
//    ofstream out ("small-1.out", ios::out);
    ifstream in ("A-large.in", ios::in);
    ofstream out ("A-large.out", ios::out);
    in >> t;
    for (int k=1; k <= t; k++) {
        in >> x;
        out << "Case #" << k << ": ";
        if (x == 0) {
            out << "INSOMNIA";
        } else {
            bool sleep = false;
            int end_i, last_digit;
            for (end_i = 0; end_i < 20; end_i++) {
                tracker[end_i] = end_i;
            }
            end_i = 19;
            int num = 0;
            while (end_i > 9) {
                num += x;
                int tmp = num;
                while (end_i > 9 && tmp != 0) {
                    last_digit = tmp % 10;
                    tmp /= 10;
                    if (last_digit == tracker[last_digit]) {
                        swap(tracker[last_digit], tracker[end_i--]);
                    }
                }
            }
            out << num;
        }
        out << endl;
    }
    out.close();
    in.close();
    return 0;
}
