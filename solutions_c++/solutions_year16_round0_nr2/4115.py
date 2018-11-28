#include <iostream>

int main(int argc, char* argv[]) {
    int n;
    int curr;
    std::cin >> n;
    std::string cakes;
    for (int i = 0; i < n; i++) {
        bool minus = false;
        int flips = 0;
        std::cin >> cakes;
        for (int j = 0; j < cakes.length(); j++) {
            if (cakes[j] == '-' && !minus) { 
                minus = true;
                if (j == 0) {
                    flips++;
                } else {
                    flips += 2;
                }
            } else if(cakes[j] == '+' && minus) {
                minus = false;
            }    
        }
        std::cout << "Case #" << i + 1 << ": " << flips << "\n";
    }
}
