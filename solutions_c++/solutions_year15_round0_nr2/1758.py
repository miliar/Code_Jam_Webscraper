#include <algorithm>
#include <iostream>
#include <valarray>

int FindConsumptionTime(const std::valarray<int>& plates) {
    int result = plates.max();
    for (int time = 2; time < result; ++time) {
        result = std::min(result, time + ((plates - 1) / time).sum());
    }
    return result;
}


int main() {
    int number_of_cases;
    std::cin >> number_of_cases;
    
    for (int case_no = 0; case_no < number_of_cases; ++case_no) {
        int number_of_plates;
        std::cin >> number_of_plates;
        
        std::valarray<int> plates(number_of_plates);
        for (auto& plate : plates) {
            std::cin >> plate;
        }

        std::cout << "Case #" << (case_no + 1) << ": " << FindConsumptionTime(std::move(plates)) << '\n';
    }
    return 0;
}
