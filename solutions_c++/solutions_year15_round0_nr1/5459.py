#include <iostream>
#include <vector>
#include <string>

typedef std::vector<int> VI;

int main() {
    int T;
    std::cin >> T;

    int C = 1;
    while(T--) {
        VI members;
        int max;
        std::cin >> max;

        std::string s;
        std::cin >> s;
        int additional = 0;
        int count = 0;
        for(int i = 0; i < max; i ++) {
            count += (s[i]-'0');
            while(count <= i) additional ++, count ++;
        }
        
        std::cout << "Case #" << (C++) <<": " << additional << std::endl;
    }

    return 0;
}
