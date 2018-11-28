#include "codejam.h"

/*

0123456789
+-+-

*/

class Pancake : public CodeJam {
public:
    void solve(const string input) {
        int count = 0;
        string s = input;
        int i = s.size() - 1;

        while (true) {
            while (i >= 0 && s[i] == '+') i--;
            if (i < 0) {
                // Done
                output(count);
                return;
            }

            count++;
            for (int j = 0; j <= i; j++) {
                if (s[j] == '-') {
                    s[j] = '+';
                } else {
                    s[j] = '-';
                }
            }
            //printf("%s\n", s.c_str());
        }
    }
};

int main (void)
{
    Pancake p;
    p.parseInput();
    //p.dumpInput();
    p.solveAll();
    p.dumpOutput();

    return 0;
}
