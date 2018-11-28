#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;

int main()
{
    int T;
    ifstream ifs("input.txt");
    ofstream ofs("out.txt");
    ifs >> T;
    int first[4][4],second[4][4],fRow,sRow;
    int answer = 0;
    for (int i = 0; i < T; i++)
    {
        int count = 0;
        ifs >> fRow;
        for (int j = 0; j < 4; j++) {
            for (int z = 0; z < 4; z++) {
                ifs >> first[j][z];
            }
        }
        ifs >> sRow;
        for (int j = 0; j < 4; j++) {
            for (int z = 0; z < 4; z++) {
                ifs >> second[j][z];
            }
        }
        fRow--;
        sRow--;
        for (int y = 0; y < 4; y++) {
            for (int z = 0; z < 4; z++) {
                if (first[fRow][y] == second[sRow][z]) {
                    count++;
                    answer = second[sRow][z];
                }
            }
        }
        switch (count) {
            case 0:
                ofs << "Case #" << (i + 1) << ": Volunteer cheated!" << endl;
                break;
            case 1:
                ofs << "Case #" << (i+1) << ": " << answer<<endl;
                break;
            default:
                ofs << "Case #" << (i + 1) << ": Bad magician!" << endl;
                break;
        }
    }
}