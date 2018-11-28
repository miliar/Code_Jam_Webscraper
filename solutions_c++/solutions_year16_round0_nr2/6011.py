//
//  main.cpp
//  codejam
//
//  Created by 원재 정 on 2016. 4. 9..
//  Copyright © 2016년 Anthony Jung. All rights reserved.
//

#include <iostream>
#include <string>
#include <bitset>
#include <fstream>

bool check_done(const std::bitset<100>& bits, size_t count) {
    return (bits.count() == count);
}

void filp(std::bitset<100>& bits, size_t index) {
    for (size_t i = 0; i < index; ++i) {
        bits.flip(i);
    }
}

size_t find_flip_point(const std::bitset<100>& bits, size_t start_index, size_t length) {
    auto bit = bits[start_index];
    for (auto i = start_index + 1; i < length; ++i) {
        if (bits[i] != bit)
            return i;
    }
    return length;
}

std::bitset<100> convert_bitstring(const std::string& s) {
    std::bitset<100> bits;
    for (size_t i = 0, ii = s.length(); i < ii; ++i) {
        bits[i] = (s[i] == '+');
    }
    return std::move(bits);
}

int find_minimum_flip_count(const std::string& s) {
    auto bits = convert_bitstring(s);
    auto length = s.length();
    size_t start_index = 0;
    int count = 0;
    while(!check_done(bits, length)) {
        auto point = find_flip_point(bits, start_index, length);
        filp(bits, point);
        count++;
        start_index = point;
    }
    return count;
}

int main(int argc, const char * argv[]) {
    int t;
    std::ifstream fin("B-large.in");
    std::ofstream fout("B-large.out");
    fin >> t;
    for (int i = 1; i <= t; ++i) {
        std::string s;
        fin >> s;
        fout << "Case #" << i << ": " << find_minimum_flip_count(s) << std::endl;
    }
    fin.close();
    fout.close();
    
    return 0;
}
