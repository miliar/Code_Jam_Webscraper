#include <algorithm>
#include <iostream>
#include <vector>


int ComputeNumberOfDiscs(int disc_capacity, std::vector<int> files_sizes) 
{
    int result = 0;
    std::sort(files_sizes.begin(), files_sizes.end());
    auto it = files_sizes.begin();
    auto jt = files_sizes.end();
    while (it + 1 < jt) {
        if (it[0] + jt[-1] <= disc_capacity) {
            ++it;
            --jt;
        } else {
            --jt;
        }
        ++result;
    }
    if (it + 1 == jt) {
        ++result;
    }
    return result;
}


int main()
{
    int number_of_cases;
    std::cin >> number_of_cases;
    for (int case_no = 1; case_no <= number_of_cases; ++case_no) {
        int number_of_files, disc_capacity;
        std::cin >> number_of_files >> disc_capacity;
        std::vector<int> files_sizes(number_of_files, 0);
        for (int& file_size : files_sizes) {
            std::cin >> file_size;
        }
        std::cout << "Case #" << case_no << ": " << ComputeNumberOfDiscs(disc_capacity, files_sizes) << '\n';
    }
    return 0;
}
