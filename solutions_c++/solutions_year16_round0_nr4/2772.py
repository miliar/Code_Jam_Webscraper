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

#define LEAD 'L'
#define GOLD 'G'

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

std::string next_sequence(std::string sequence) {
    int i = sequence.size()-1;
    
    while (true) {
        if(sequence[i] == LEAD) {
            sequence[i] = GOLD;
            break;
        }
        else {
            sequence[i] = LEAD;
            i--;
        }
    }
    
    return sequence;
}

std::string increase_complexity(std::string sequence, std::string original_sequence) {
    std::string new_sequence("");
    
    for (std::string::iterator it = sequence.begin(); it != sequence.end(); it++) {
        if ((*it) == GOLD) {
            new_sequence.append(std::string(original_sequence.size(), GOLD));
        }
        else {
            new_sequence.append(original_sequence);
        }
    }
    
    return new_sequence;
}

std::string sequence_of_complexity(std::string original_sequence, int C) {
    std::string sequence = original_sequence;
    
    for (int i = 1; i < C; i++) {
        sequence = increase_complexity(sequence, original_sequence);
    }
    
    return sequence;
}

std::string calculate_solution(int K, int C, int S) {
    std::string output = "";
    
    if (K == S) {
        output += "1";
        for (int i = 2; i <= S; i++) {
            output += " ";
            output += std::to_string(i);
        }
        return output;
    }

    int count = std::pow(2,K);
    std::string sequence(K, LEAD);
    
    std::cout << sequence_of_complexity(sequence,C) << std::endl;
    
    for (int i = 1; i < count; i++) {
        sequence = next_sequence(sequence);
        
        std::cout << sequence_of_complexity(sequence,C) << std::endl;
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
        std::string solution = calculate_solution(std::stoi(tokens[0]), std::stoi(tokens[1]), std::stoi(tokens[2]));
        
        ss << "Case #" << i+1 << ": " << solution << std::endl;
    }
    
    write_text_to_file(std::string("output.txt"), ss.str());
    
    return 0;
}