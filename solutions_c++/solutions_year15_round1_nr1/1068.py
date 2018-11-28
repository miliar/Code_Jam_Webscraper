#include <iostream>
#include <vector>


void run_test_case()
{
    int result_1 = 0;
    int result_2 = 0;

    int N;
    std::cin >> N;

    std::vector<int> ms;

    for (int i = 0; i < N; ++i) {
        int m;
        std::cin >> m;
        ms.push_back(m);
    }

    int max_d = 0;
    for (int i = 1; i < N; ++i) {
        if (ms[i-1] > ms[i]) {
            int d = ms[i-1] - ms[i];
            result_1 += d;
            if (d > max_d) {
                max_d = d;
            }
        }
    }

    for (int i=0; i < N-1; ++i) {
        result_2 += std::min(ms[i], max_d);
    }

    std::cout << result_1 << " " << result_2;
}


int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        std::cout << "Case #" << t << ": ";
        run_test_case();
        std::cout << '\n';
    }

    return 0;
}
