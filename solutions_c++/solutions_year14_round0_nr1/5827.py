#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main() {
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    
    int numCases;
    fin >> numCases;
    
    for (int i = 0; i < numCases; i++) {
        int firstAnswer, secondAnswer;
        vector<int> first(4, -1);
        fin >> firstAnswer;
        
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                int thisVal;
                fin >> thisVal;
                if (j == (firstAnswer - 1))
                    first[k] = thisVal;
            }
        }
        
        sort(first.begin(), first.end());
        
        fin >> secondAnswer;
        
        int answer = -1;
        int numTogether = 0;
        
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                int thisVal;
                fin >> thisVal;
                if (j == (secondAnswer - 1) && binary_search(first.begin(), first.end(), thisVal)) {
                    answer = thisVal;
                    numTogether++;
                }
            }
        }
        
        if (numTogether == 0)
            fout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
        else if (numTogether == 1)
            fout << "Case #" << i+1 << ": " << answer << endl;
        else
            fout << "Case #" << i+1 << ": Bad magician!" << endl;
    }
    
	return 0;
}