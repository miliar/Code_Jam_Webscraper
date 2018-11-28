#include <iostream>


//=====================================================================================
int main() {
    int x;
    int waste;
    std::cin >> x;
    for(int i = 0; i < x; i++) {
        int array1[4];
        int array2[4];
        int row;
        std::cin >> row;
        for (int d = 1; d < row; d++) {
            std::cin >> waste;
            std::cin >> waste;
            std::cin >> waste;
            std::cin >> waste;
        }
        for (int it = 0; it < 4; it++)
            std::cin >> array1[it];

        for (int l = 0; l < (4-row)*4; l++)
            std::cin >> waste;

        std::cin >> row;
        for (int d = 1; d < row; d++) {
            std::cin >> waste;
            std::cin >> waste;
            std::cin >> waste;
            std::cin >> waste;
        }
        for (int it = 0; it < 4; it++)
            std::cin >> array2[it];

        for (int l = 0; l < (4-row)*4; l++)
            std::cin >> waste;

        int count = 0;
        int store;
        for (int jk = 0; jk < 4; jk++) {
            int val1 = array1[jk];
            for (int lm = 0; lm < 4; lm++) {
                    int val2 = array2[lm];
                    if (val1 == val2){
                        count++;
                        store = val1;
                    }
            }
        }
        std::cout << "Case #" << (i+1) << ": ";
        if (count == 0)
            std::cout << "Volunteer cheated!";
        else if(count == 1)
            std::cout << store;
        else
            std::cout << "Bad magician!";
        std::cout << std::endl;





    }
    return 0;
}
