#include <iostream>
#include <vector>
#include <utility>
#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
    ifstream input;
    ofstream output;
    
    input.open(argv[1]);
    output.open("output.out");
    
    int T, row;
    input >> T;
    
    for (int i = 0; i < T; i++) {
        bool set[16];
        for (int i = 0; i < 16; i++) {
            set[i] = false;
        }
        
        input >> row;
        for (int j = 1; j <= 4; j++) {
            for (int k = 0; k < 4; k++) {
                int tmp;
                input >> tmp;
                if (j == row) {
                   set[tmp - 1] = true;   
                }
            }
        }
        
        input >> row;
        int cnt = 0, ans;
        for (int j = 1; j <= 4; j++) {
            for (int k = 0; k < 4; k++) {
                int tmp;
                input >> tmp;
                if (j == row && set[tmp - 1] == true) {
                   cnt++;
                   ans = tmp;
                }
            }
        }
        
        output << "Case #" << i + 1 << ": ";
        if (cnt == 1) {
            output << ans;
        } else if (cnt > 1) {
            output << "Bad magician!";  
        } else if (cnt == 0) {
            output << "Volunteer cheated!";
        }
        
        if ((i + 1) != T) {
            output << endl;
        }
    }
}
