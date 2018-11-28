#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

std::vector<int> split(std::string&);
int max(const std::vector<int>&);

int main() {
    std::string line;
    std::ifstream f("B-large.in");
    getline(f, line);

    int total = std::stoi(line);
    if (f.is_open()) {
        for (int i = 0; i < total; ++i) {
            getline(f, line);
            int diners = std::stoi(line);

            getline(f, line);
            std::vector<int> plates = split(line); 
            // for (auto& i:plates) {
            //     std::cout << i << " ";
            // }
            // std::cout << std::endl;

            /* brute force search */
            int min_time = 65535;
            for (int remain_time = 1; remain_time <= max(plates); ++remain_time) {
                int total_time = remain_time;
                for (int j = 0; j < plates.size(); ++j) {
                    total_time += ceil((double)plates[j] / (double)remain_time) - 1; 
                }
                min_time = total_time < min_time ? total_time : min_time; 
            } 
            std::cout << "Case #" << i+1 << ": " << min_time << std::endl; 
        }
    }
}

std::vector<int> split(std::string& s) {
    int begin = 0;
    std::vector<int> vec;
    for (int i = 0; i <= s.size(); ++i) {
        if (s[i] == ' ' || i == s.size()) {
            vec.push_back(std::stoi(s.substr(begin, i-begin))); 
            begin = i+1; 
        }
    }
    return vec;
}

int max(const std::vector<int>& vec) {
    int m = 0;
    for (auto& i: vec) {
        m = i > m ? i : m;
    }
    return m;
} 
