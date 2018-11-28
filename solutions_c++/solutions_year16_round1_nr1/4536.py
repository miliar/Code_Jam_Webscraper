//
//  main.cpp
//  TheLastWord
//
//  Created by 원재 정 on 2016. 4. 16..
//  Copyright © 2016년 Anthony Jung. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

std::string get_last_word(const std::string& s) {
    std::string last_word(1, s[0]);
    std::stringstream ss;
    for (size_t i = 1, length = s.length(); i < length; ++i) {
        if (last_word[0] > s[i])
            ss << last_word << s[i];
        else
            ss << s[i] << last_word;
        last_word = ss.str();
        ss.str("");
    }
    return move(last_word);
}

int main(int argc, const char * argv[]) {
    int t;
    std::ifstream fin("A-small-attempt0.in");
    std::ofstream fout("A-small-attempt0.out");
    fin >> t;
    for (int i = 1; i <= t; ++i) {
        std::string s;
        fin >> s;
        fout << "Case #" << i << ": " << get_last_word(s) << std::endl;
    }
    fin.close();
    fout.close();
    return 0;
}
