//
//  Training.cpp
//  
//
//  Created by Tobias Hecht on 11.03.15.
//
//

#include <string>
#include <iostream>
#include <cmath>
#include <cstring>
#include <set>
#include <vector>
#include <fstream>
#include <sstream>

#define HAPPY '+'
#define UNHAPPY '-'

std::vector<std::string> tokenize_string(std::string str, const char* delimiters) {
    std::vector<std::string> ret_vec;
    char * pch;
    pch = std::strtok((char*)str.c_str(), delimiters);
    while(pch != NULL) {
        ret_vec.push_back(std::string(pch));
        pch = std::strtok(NULL, delimiters);
    }
    return ret_vec;
}

std::string get_text_from_file(std::string filename) {
    std::string text;
    std::string line;
    
    std::ifstream file(filename);
    
    while(std::getline(file,line)) {
        text += line;
        text += "\n";
    }
    
    return text;
}

void write_text_to_file(std::string filename, std::string text) {
    std::ofstream file;
    file.open(filename);
    file << text;
    file.close();
}

long smallest_divisor(long number) {
    long upper_limit = static_cast<long>(std::sqrt(static_cast<double>(number)))+1;
    
    for (long i = 2; i < upper_limit; i++) {
        if (number%i == 0) {
            return i;
        }
    }
    
    return 1;
}

long number_to_base(std::string input, int base) {
    long ret_number = 0;
    long power = 1;
    for (std::string::reverse_iterator it = input.rbegin(); it != input.rend() ; it++) {
        ret_number += power* static_cast<long>((*it)-'0');
        
        power *= base;
    }
    
    return ret_number;
}

std::string calculate_jamcoin(std::string input) {
    std::string ret = input;
    
    for (int i = 2; i <= 10; i++) {
        long number = number_to_base(input, i);
        
        long sm_div = smallest_divisor(number);
        
        if (sm_div == 1) {
            return std::string("");
        }
        else {
            ret += " " + std::to_string(sm_div);
        }
    }
    
    return ret;
}

std::string next_jamcoin_candidate(std::string input) {
    int i = input.size()-2;
    
    while (true) {
        if(input[i] == '0') {
            input[i] = '1';
            break;
        }
        else {
            input[i] = '0';
            i--;
        }
    }
    
    return input;
}

std::string calculate_solution(int length, int number) {
    int found_jamcoins = 0;
    std::string output = "";
    std::string canditate(length, '0');
    canditate[0] = '1';
    canditate[canditate.size()-1] = '1';
    
    while (found_jamcoins < number) {
        std::string return_string = calculate_jamcoin(canditate);
        
        if (return_string.size() > 0) {
            output += "\n" + return_string;
            
            found_jamcoins++;
        }
        
        canditate = next_jamcoin_candidate(canditate);
    }
    
    return output;
}

int main() {
    std::string text = get_text_from_file("input.txt");
    
    std::vector<std::string> lines = tokenize_string(text, "\n");
    std::stringstream ss;
    int count = stoi(lines[0]);
    
    for (int i = 0; i < count; i++) {
        std::vector<std::string> tokens = tokenize_string(lines[i+1], " ");
        std::string solution = calculate_solution(std::stoi(tokens[0]), std::stoi(tokens[1]));
        
        ss << "Case #" << i+1 << ":";
        ss << solution;
    }
    ss << "\n";
    
    write_text_to_file(std::string("output.txt"), ss.str());
    
    return 0;
}