#include <iostream>
#include <vector>
#include <algorithm>

static void solve(int case_no)
{
    int n1;
    std::cin >> n1;
    std::vector<int> d1(16);
    for (int i = 0; i < 16; ++i) {
        std::cin >> d1[i];
    }
    int n2;
    std::cin >> n2;
    std::vector<int> d2(16);
    for (int i = 0; i < 16; ++i) {
        std::cin >> d2[i];
    }
    std::vector<int> result;
    std::sort(&d1[(n1-1)*4], &d1[n1*4]);
    std::sort(&d2[(n2-1)*4], &d2[n2*4]);
    std::set_intersection(
            &d1[(n1-1)*4], &d1[n1*4],
            &d2[(n2-1)*4], &d2[n2*4],
            std::back_inserter(result)
        );
    std::cout << "Case #" << case_no << ": ";
    if (result.size() == 0) {
        std::cout << "Volunteer cheated!";
    } else if (result.size() == 1) {
        std::cout << result[0];
    } else {
        std::cout << "Bad magician!";
    }
    std::cout << std::endl;
}

int main()
{
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
    return 0;
}
