#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <cstdio>


int solution(const std::string& s) {
    int friends = 0;
    int clapping_people = 0;

    for (int i = 0; i < s.size(); ++i) {
        int next_wave = (int)((char)s[i] - '0');

        if (i > clapping_people) {
            friends += (i - clapping_people);
            clapping_people = i;
        }
        clapping_people += next_wave;
    }
    
    return friends;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    std::cin >> t;
    for (size_t i = 0; i < t; ++i) {
        int k;
        std::string s;

        std::cin >> k;
        std::cin >> s;
        
        std::cout << "Case #" << i + 1 << ": "<< solution(s) << '\n';
    }
}
