#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector> 
#include <cstdint>

using namespace std;

void generate(uint64_t num, std::set<uint64_t> & nums) {
    while (num != 0) {
        uint64_t val = num % 10;
        nums.insert(val);
        num /= 10;
    }
}

int find_last_number(uint64_t num) {
    std::set<uint64_t> nums;
    generate(num, nums);

    uint64_t value = num;
    while(nums.size() < 10) {
        //std::cout << "For " << num << " we have a size of " << nums.size() << endl;
        value += num;
        generate(value, nums);
    }

    return value;
}

int main(int argc, char **argv) {
    int tests;
    cin >> tests;

    for (int i = 1; i <= tests; i++) {
        uint64_t num;
        cin >> num;
       
        cout << "Case #" << i << ": ";
        if (num == 0) {
            cout << "INSOMNIA" << endl;
        } else {
            cout << find_last_number(num) << endl;
        }
    }
    
    return 0;
}



