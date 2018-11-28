#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int main() {
    string test_filename;
    cout << "Enter test file : " << endl;
    getline(cin, test_filename);
    cout << endl;

    string out_name = test_filename + "_out.txt";
    ifstream in_file(test_filename.c_str());
    ofstream out_file(out_name);

    int T;
    in_file >> T;

    for(int t = 0; t < T; t++) {
        int ans1, ans2;
        int M1[4][4];
        int M2[4][4];

        in_file >> ans1;
        for(int j = 0; j < 4; j++) {
            for(int i = 0; i < 4; i++) {
                in_file >> M1[j][i];
            }
        }

        in_file >> ans2;
        for(int j = 0; j < 4; j++) {
            for(int i = 0; i < 4; i++) {
                in_file >> M2[j][i];
            }
        }

        int possible[16];
        for(int i = 1; i <= 16; i++) {
            possible[i-1] = 0;
        }

        for(int i = 0; i < 4; i++) {
            possible[M1[ans1-1][i]-1]++;
        }

        for(int i = 0; i < 4; i++) {
            possible[M2[ans2-1][i]-1]++;
        }

        vector<int> solutions;
        for(int i = 0; i < 16; i++) {
            if(possible[i] == 2) {
                solutions.push_back(i+1);
            }
        }


        out_file << "Case #" << t + 1 << ": ";

        if(solutions.size() == 0) {
            out_file << "Volunteer cheated!" << endl;
        }
        else if(solutions.size() == 1) {
            out_file << solutions[0] << endl;
        }
        else {
            out_file << "Bad magician!" << endl;
        }
    }
    out_file.close();
}