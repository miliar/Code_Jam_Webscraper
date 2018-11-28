#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream input;
    ofstream output;
    output.open("out.txt");
    input.open("A-small-attempt1.in");
    int t;
    input >> t;
    int i = 0;
    while(i < t){
        int line1, line2;
        input >> line1;
        int numbers1[4][4], numbers2[4][4];
        input >> numbers1[0][0] >> numbers1[0][1] >> numbers1[0][2] >> numbers1[0][3];
        input >> numbers1[1][0] >> numbers1[1][1] >> numbers1[1][2] >> numbers1[1][3];
        input >> numbers1[2][0] >> numbers1[2][1] >> numbers1[2][2] >> numbers1[2][3];
        input >> numbers1[3][0] >> numbers1[3][1] >> numbers1[3][2] >> numbers1[3][3];
        input >> line2;
        input >> numbers2[0][0] >> numbers2[0][1] >> numbers2[0][2] >> numbers2[0][3];
        input >> numbers2[1][0] >> numbers2[1][1] >> numbers2[1][2] >> numbers2[1][3];
        input >> numbers2[2][0] >> numbers2[2][1] >> numbers2[2][2] >> numbers2[2][3];
        input >> numbers2[3][0] >> numbers2[3][1] >> numbers2[3][2] >> numbers2[3][3];
        int num = 0, mark = 0;
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                if(numbers1[line1 - 1][j] == numbers2[line2 - 1][k]){
                    num++;
                    mark = numbers1[line1 - 1][j];
                }
            }
        }
        if(num == 1){
            output << "Case #" << i + 1 << ": " << mark << endl;
        }
        else if(num == 0){
            output << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
        }
        else{
            output << "Case #" << i + 1 << ": Bad magician!" << endl;
        }
        i++;
    }
    input.close();
    output.close();
    return 0;
}
