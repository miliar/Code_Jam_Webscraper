#include <iostream>
#include <string>
#include <bitset>
#include <vector>
#include <algorithm>

bool has(std::string s, std::string p) {
    for (char ch : p) {
        if (s.find(ch) == std::string::npos) {
            return false;
        } else {
            s.erase(s.find_first_of(ch), 1);
        }
    }
    return true;
}

bool remove(std::string &s, std::string p) {
    std::string new_string = "";
    int index = 0;
    for (char ch : s) {
        
//        std::cout << ch << std::endl;
        if (p.find(ch) == std::string::npos) {
            new_string += ch;
        } else {
            index++;
            p.erase(p.find_first_of(ch), 1);
        }
        //index++;
    }
    s = new_string;
    return true;
}

std::string get_number(std::string l) {
    std::string num = "";
    int len = l.length();
    while (l.length() > 0) {
//        std::cout << l  << " " << num << std::endl;
        if (has(l, "ZERO")) {
            num += "0";
            remove(l, "ZERO");
        } else if (has(l, "SIX")) {
            num += "6";
            remove(l, "SIX");
        } else if (has(l, "SEVEN")) {
            num += "7";
            remove(l, "SEVEN");
        } else if (has(l, "TWO")) {
            num += "2";
            remove(l, "TWO");
        } else if (has(l, "EIGHT")) {
            num += "8";
            remove(l, "EIGHT");
        } else if (has(l, "FOUR")) {
            num += "4";
            remove(l, "FOUR");
        } else if (has(l, "THREE")) {
            num += "3";
            remove(l, "THREE");
        } else if (has(l, "FIVE")) {
            num += "5";
            remove(l, "FIVE");
        } else if (has(l, "NINE")) {
            num += "9";
            remove(l, "NINE");
        } else if (has(l, "ONE")) {
            num += "1";
            remove(l, "ONE");
        }
    }
    std::sort(num.begin(), num.end());
    return num;
}

int main() {
    int t;
    std::string n;
    std::cin >> t;  // read T
    for (int i = 1; i <= t; ++i) {
        std::cin >> n;  // read N
        std::cout << "Case #" << i << ": " << get_number(n) << std::endl;
    }
}
