#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
    int n;
    int k;
    int c;
    int s;
    std::cin >> n;
    
    for (int i = 0; i < n; i++) {
        std::cin >> k >> c >> s;
        std::string output = "";
        for (int j = 1; j <= s; j++) {
            output += std::to_string(j) + " ";
        }
        std::cout << "Case #" << i + 1 << ": " << output << "\n";
    }
}
