/*
 * A.CountingSheep.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: piotr
 */

#include <algorithm>
#include <bitset>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

using sol_type = string;
long long int input = -1;

sol_type find_solution();

int main() {

    int cases;
    int case_num =0;

    cin >> cases;

    while (cases--) {
        ++case_num;
        cin >> input;
        auto solution = find_solution();
        cout << "Case #" << case_num << ": ";
        cout << solution << endl;
    }
    return 0;
}

sol_type find_solution(){
    assert(input >= 0);
    bitset<10> digits;
    if (input == 0)
        return "INSOMNIA";
    auto number = input;
    while(true) {
        auto s = to_string(number);
        for(int i = 0; i<10; ++i)
            if(!digits[i] && s.find('0'+i) != s.npos)
                digits[i] = 1;
        if(digits.all())
            break;
        number += input;
    }
    return to_string(number);
}
