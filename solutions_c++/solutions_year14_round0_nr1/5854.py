#include <iostream>
#include <fstream>

int main(int argc, char * argv[]){
    if (argc != 2){
        return 1;
    }

    std::ifstream in(argv[1]);
    if (!in){
        return 2;
    }

    std::ofstream out("out");

    int T; in >> T;
    for(int i = 0; i < T; i++){
        int row1, row2, grid1[4], grid2[4];
        in >> row1;
        for(int j = 1; j < 5; j++){
            for (int k = 0; k < 4; k++){
                int t; in >> t;
                if (j == row1){
                    grid1[k] = t;
                }
            }
        }

        in >> row2;
        for(int j = 1; j < 5; j++){
            for (int k = 0; k < 4; k++){
                int t; in >> t;
                if (j == row2){
                    grid2[k] = t;
                }
            }
        }

        int same = 0, value;
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                if (grid1[j] == grid2[k]){
                    same++;
                    value = grid1[j];
                }
            }
        }

        out << "Case #" << i + 1 << ": ";
        if (same == 1){
            out << value;
        }
        else if (same == 0){
            out << "Volunteer cheated!";
        }
        else{
            out << "Bad magician!";
        }
        out << std::endl;
    }

    return 0;
}
