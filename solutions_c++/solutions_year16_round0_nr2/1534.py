/*
 * B.RevengeofthePancakes.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: piotr
 */

#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

using sol_type = int;

sol_type find_solution();
string input;

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
    int ret = (*input.crbegin() == '-') ? 1 : 0;
    for(auto i = 1u; i < input.size(); ++i)
        if(input[i-1] != input[i])
            ++ret;
    return ret;
}



