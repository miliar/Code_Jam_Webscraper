#include <iostream>

int main(void)
{
    int t;
    std::cin >> t;
    for (int iii = 0; iii < t; ++iii) {
        int n;
        std::cin >> n;
        bool seen[10] = {false};
        if (n == 0) {
            std::cout << "Case #" << iii+1 << ": INSOMNIA" << std::endl;
            continue;
        }
        int i = 0;
        // int times = 0;
        while (true) {
            int m = n*(++i);
            while (m > 0) {
                seen[m % 10] = true;
                m /= 10;
            }
            int j;
            for (j = 0; j < 10; ++j) {
                if (!seen[j]) break;
            }
            if (j == 10) {
                std::cout << "Case #" << iii+1 << ": " << n*i << std::endl;
                break;
            }
            // times++;
            // if (times > 100) {
            //     std::cout << "Times > 100" << std::endl;
            // }
        }
    }
    return 0;
}
