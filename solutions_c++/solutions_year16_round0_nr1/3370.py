//
//  Training.cpp
//  
//
//  Created by Tobias Hecht on 11.03.15.
//
//

#include <string>
#include <iostream>
#include <cstring>
#include <set>
#include <vector>
#include <fstream>
#include <sstream>

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

std::string calculate_solution(std::string str_number) {
    long number = stoi(str_number);
    
    if(number == 0) {
        return std::string("INSOMNIA");
    }
    
    std::set<char> digit_collection(str_number.begin(), str_number.end());
    
    long temp_number = number;
    
    while (digit_collection.size() < 10) {
        temp_number += number;
        
        std::string temp_str_number = std::to_string(temp_number);
        
        digit_collection.insert(temp_str_number.begin(), temp_str_number.end());
    }
    
    return std::to_string(temp_number);
}

int main() {
    std::string text = get_text_from_file("input.txt");
    
    std::vector<std::string> lines = tokenize_string(text, "\n");
    std::stringstream ss;
    int count = stoi(lines[0]);
    
    for (int i = 0; i < count; i++) {
        std::string solution = calculate_solution(lines[i+1]);
        
        ss << "Case #" << i+1 << ": " << solution << std::endl;
    }
    
    write_text_to_file(std::string("output.txt"), ss.str());
    
    return 0;
}