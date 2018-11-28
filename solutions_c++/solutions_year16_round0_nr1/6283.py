#include "codejam.h"

class CountingSheep : public CodeJam {
public:
    void solve(void) {
        for (int i = 0; i < _input.size(); i++) {
            int digits[10] = { 0 };
            int seen = 0;
            int n = atoi(_input[i].c_str());
            int mul = 0;
            //printf("n = %d\n", n);

            while (seen != 10) {
                int num = ++mul * n;
                if (mul > 1 && num == n) {
                    _output.push_back("INSOMNIA");
                    break;
                }

                char str[1024];
                snprintf(str, sizeof(str), "%d", num);
                //printf("str = %s\n", str);

                for (int j = 0; j < strlen(str); j++) {
                    int digit = str[j] - '0';
                    //printf("%s %d\n", str, digit);
                    if (!digits[digit]) {
                        digits[digit]++;
                        if (++seen == 10) {
                            _output.push_back(str);
                            break;
                        }
                    }
                }
            }
        }
    }
};

int main (void)
{
    CountingSheep cs;
    cs.parseInput();
    //cs.dumpInput();
    cs.solve();
    cs.dumpOutput();
    return 0;
}
