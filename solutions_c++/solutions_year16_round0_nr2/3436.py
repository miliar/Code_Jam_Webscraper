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

std::string flip(std::string pancakes, int number) {
    std::string retValue = pancakes;
    
    for (int i = 0; i < number; i++) {
        retValue[number-i-1] = pancakes[i] == HAPPY ? UNHAPPY : HAPPY;
    }
    
    return retValue;
}

bool all_pancakes_happy(std::string pancakes) {
    for (std::string::iterator it = pancakes.begin(); it != pancakes.end(); it++) {
        if ((*it) != HAPPY) {
            return false;
        }
    }
    
    return true;
}

std::string calculate_solution(std::string pancakes) {
    int flips = 0;
    
    while (!all_pancakes_happy(pancakes)) {
        char top = pancakes[0];
        
        int index = 0;
        while (pancakes[index] == top) {
            if (index >= pancakes.size()) {
                // Each pancake is upside down
                break;
            }
            index++;
        }
        
        pancakes = flip(pancakes, index);
        flips++;
    }
    
    return std::to_string(flips);
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