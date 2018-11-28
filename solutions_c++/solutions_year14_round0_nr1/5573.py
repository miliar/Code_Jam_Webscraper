#include <iostream>
#include <vector>
#include <set>

typedef std::vector<int> VI;
typedef std::vector<VI> VVI;

int main() {
    int T;
    std::cin >> T;
    int C = 1;
    while(T--) {
        int r1, r2;
        std::cin >> r1;
        VVI grid1(4, VI(4,0));
        for(int j = 0; j < 4; j ++) for(int i = 0; i < 4; i ++) std::cin >> grid1[j][i];
        std::cin >> r2;
        VVI grid2(4, VI(4,0));
        for(int j = 0; j < 4; j ++) for(int i = 0; i < 4; i ++) std::cin >> grid2[j][i];

        std::set<int> possibles;
        int p = -1;
        for(int i = 0; i < 4; i ++) possibles.insert(grid1[r1-1][i]);
        for(int i = 0; i < 4; i ++) {
            int tr = grid2[r2-1][i];
            if(possibles.count(tr) != 0) {
                if(p == -1) p = tr;
                else p = -2;
            }
        }

        std::cout << "Case #" << C << ": ";
        C ++;
        if(p == -1) std::cout << "Volunteer cheated!" << std::endl;
        else if(p == -2) std::cout << "Bad magician!" << std::endl;
        else std::cout << p << std::endl;
    }
    return 0;
}
