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

typedef int number;
typedef unsigned int u_number;
typedef vector<number> vec_number;
typedef set<number> set_number;
typedef vector<u_number> vec_u_number;
typedef set<u_number> set_u_number;
typedef vector<string> vec_string;
typedef set<string> set_string;

string calculate_solution(string line) {
    int number_of_0 = count(line.begin(), line.end(), 'Z');
    int number_of_8 = count(line.begin(), line.end(), 'G');
    int number_of_6 = count(line.begin(), line.end(), 'X');
    int number_of_2 = count(line.begin(), line.end(), 'W');
    int number_of_4 = count(line.begin(), line.end(), 'U');
    int number_of_7 = count(line.begin(), line.end(), 'S')-number_of_6;
    int number_of_5 = count(line.begin(), line.end(), 'V')-number_of_7;
    int number_of_3 = count(line.begin(), line.end(), 'R')-number_of_4-number_of_0;
    int number_of_1 = count(line.begin(), line.end(), 'O')-number_of_0-number_of_2-number_of_4;
    int number_of_9 = count(line.begin(), line.end(), 'I')-number_of_5-number_of_6-number_of_8;
    
    string retValue = string("");
    for(int i = 0; i < number_of_0; i++) {
        retValue += string("0");
    }
    
    for(int i = 0; i < number_of_1; i++) {
        retValue += string("1");
    }
    
    for(int i = 0; i < number_of_2; i++) {
        retValue += string("2");
    }
    
    for(int i = 0; i < number_of_3; i++) {
        retValue += string("3");
    }
    
    for(int i = 0; i < number_of_4; i++) {
        retValue += string("4");
    }
    
    for(int i = 0; i < number_of_5; i++) {
        retValue += string("5");
    }
    
    for(int i = 0; i < number_of_6; i++) {
        retValue += string("6");
    }
    
    for(int i = 0; i < number_of_7; i++) {
        retValue += string("7");
    }
    
    for(int i = 0; i < number_of_8; i++) {
        retValue += string("8");
    }
    
    for(int i = 0; i < number_of_9; i++) {
        retValue += string("9");
    }
    
    return retValue;
}

int main() {
    number count;
    
    cin >> count;
    
    for (number i = 0; i < count; i++) {
        string line;
        cin >> line;
        string solution = calculate_solution(line);
        
        cout << "Case #" << i+1 << ": " << solution << endl;
    }
    
    return 0;
}