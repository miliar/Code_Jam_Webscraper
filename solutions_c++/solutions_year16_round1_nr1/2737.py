//
//  CodeJam.cpp
//  
//
//  Created by Tobias Hecht on 15.04.15.
//
//

#include <algorithm>
#include <string>
#include <iostream>
#include <cmath>
#include <cstring>
#include <set>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

typedef long number;
typedef unsigned long u_number;
typedef vector<number> vec_number;
typedef set<number> set_number;
typedef vector<u_number> vec_u_number;
typedef set<u_number> set_u_number;
typedef vector<string> vec_string;
typedef set<string> set_string;

string calculate_solution(string a) {
    string retValue = string(1,a[0]);
    for (int i = 1; i < a.length(); i++) {
        char x = retValue[0];
        char y = retValue[retValue.length()-1];
        char z = a[i];
        
        if (x <= z) {
            retValue = string(1,z) + retValue;
        }
        else {
            retValue = retValue + string(1,z);
        }
    }
    return retValue;
}

int main() {
    int count;
    
    cin >> count;
    
    for (int i = 0; i < count; i++) {
        string a;
        cin >> a;
        string solution = calculate_solution(a);
        
        cout << "Case #" << i+1 << ": " << solution << endl;
    }
    
    return 0;
}