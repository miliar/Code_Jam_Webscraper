#include <iostream>

void run(int casenum) {
    int n;
    std::cin >> n;

    int curr_up = 0;
    int should_add = 0;

    for (int curr = 0; curr <= n; ++curr) {
        char i;
        std::cin >> i;
        int c = i - '0';
        if (curr == 0) // first
            curr_up += c;
        else if (c > 0) {
            if (curr_up < curr) {
                should_add += curr - curr_up;
                curr_up = curr;
            }
            curr_up += c;
        }
    }

    std::cout << "Case #" << casenum << ": " << should_add << std::endl;
}

int main () {
    int n;
    std::cin >> n;
    for (int i=1; i<=n; ++i) run(i);
    return 1;
}
