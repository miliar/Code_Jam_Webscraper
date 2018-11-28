#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

#define NUM_ROWS 4

int main(int argc, char** argv){

    ofstream output_file;
    output_file.open("output.txt");
    
    ifstream infile("quals_1_input.txt");
    string line;

    // grab num cases
    getline(infile, line);
    int numCases = atoi(line.c_str());

    // for each case
    for(int i = 0; i < numCases; ++i){
        // parse board A
        getline(infile, line);
        int rowNumA = atoi(line.c_str()) - 1;
        int boardA[NUM_ROWS][NUM_ROWS];

        for(int j = 0; j < NUM_ROWS; ++j){
            getline(infile, line);
            sscanf(const_cast<char*>(line.c_str()), "%d %d %d %d", &boardA[j][0], &boardA[j][1], &boardA[j][2], &boardA[j][3]);
        }

        // parse board B
        getline(infile, line);
        int rowNumB = atoi(line.c_str()) - 1;
        int boardB[NUM_ROWS][NUM_ROWS];

        for(int j = 0; j < NUM_ROWS; ++j){
            getline(infile, line);
            sscanf(const_cast<char*>(line.c_str()), "%d %d %d %d", &boardB[j][0], &boardB[j][1], &boardB[j][2], &boardB[j][3]);
        }

        vector<int> answers;
        for(int m = 0; m < NUM_ROWS; ++m){
            for(int n = 0; n < NUM_ROWS; ++n){
                if(boardB[rowNumB][n] == boardA[rowNumA][m]){
                    answers.push_back(boardB[rowNumB][n]);
                }
            }
        }



        // print results
        output_file << "Case #" << i + 1 << ": ";
        if(answers.size() == 1){
            output_file << answers[0];
        }
        else if(answers.size() == 0){
            output_file << "Volunteer cheated!";
        }
        else{
            output_file << "Bad magician!";
        }

        output_file << endl;
    }

    output_file.close();

    return 0;
}