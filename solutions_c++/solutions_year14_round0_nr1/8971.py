#include <iostream>
#include <array>
#include <vector>

int main(int argc, char* argv[]){
    int n;
    std::cin >> n;
    const int N = n;
    while(n--){
        int fst, snd;
        std::array<std::array<int,4>,4> one;
        std::array<std::array<int,4>,4> two;
        std::cin >> fst;
        fst -= 1;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                std::cin >> one[i][j];
            }
        }
        std::cin >> snd;
        snd -= 1;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                std::cin >> two[i][j];
            }
        }

        std::vector<int> found;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if(one[fst][i] == two[snd][j]){
                    found.push_back(one[fst][i]);
                }
            }
        }
        std::cout << "Case #" << (N - n) << ": ";
        if(found.size() == 1){
            std::cout << found[0];
        }
        else if(found.size() > 1){
            std::cout << "Bad magician!";
        }
        else{
            std::cout << "Volunteer cheated!";
        }
        std::cout << std::endl;
    }
    return 0;
}