// Ken's optimal stratery: given Chosen_Naomi, Ken tries to choose the
// lightest one among those which are heavier than Chosen_Naomi, if no one is
// heavier, return the lightest one

// Naomi's optimal stratery for War: choose the block by increasing weight
// Naomi's optimal stratery for deceitful war: choose the block by inreasing weight,
// if current one is > lighest one of Ken, say its weight = heaviest of Ken + epsilon
// else, say its weight = heaviest of Ken - epsilon (epsilon=positive infinite small number)

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// calculate Naomi's score for Deceitful Way
int deceitfulWay(const vector<double> &Naomi, const vector<double> &Ken) {
    const int N = Naomi.size();
    int lo = 0;
    int hi = N - 1;
    int score = 0;
    for (int i = 0; i < N; i++) {
        if (Naomi[i] > Ken[lo]) {
            score++;
            lo++;
        }
        else hi--;
    }
    return score;
}

// calculate Naomi's score for Way
int way(const vector<double> &Naomi, const vector<double> &Ken) {
    const int N = Naomi.size();
    int lo = 0;
    int i;
    for (i = 0; i < N; i++) {
        while (lo < N && Ken[lo] < Naomi[i]) lo++;
        if (lo == N) break;
        else lo++;
    }
    return N-i;
}


int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "Need input file!" << endl;
        return 1;
    }
    ifstream input(argv[1]); // bind and open the input file
    // check whether open sucessfully
    if (!input) {
        cerr << "unable to open the input file!" << endl;
        return 1;
    }
    
    int T; // number of cases
    input >> T;
    input.ignore(256, '\n'); // ignore the rest of the line
    
    // consider each case
    for (int i = 1; i <= T; i++) {
        int N; // number of blocks
        input >> N ;
        input.ignore(256, '\n'); // ignore the rest of the line
        string line;
        // get blocks for Naomi
        vector<double> Naomi;
        getline(input, line); // get one line
        stringstream ss1(line);
        for (int j = 0; j < N; j++) {
            double wt;
            ss1 >> wt;
            Naomi.push_back(wt);
        }
        // get blocks for Ken
        vector<double> Ken;
        getline(input, line); // get one line
        stringstream ss2(line);
        for (int j = 0; j < N; j++) {
            double wt;
            ss2 >> wt;
            Ken.push_back(wt);
        }
        // sort weights
        sort(Naomi.begin(), Naomi.end());
        sort(Ken.begin(), Ken.end());
        
        // calculate Naomi's score for Deceitful Way
        int y = deceitfulWay(Naomi, Ken);
        // calculate Naomi's score for Way
        int z = way(Naomi, Ken);
        cout << "Case #" << i << ": " << y << " " << z << endl;
    }
    
    input.close(); // close file before return
    
    return 0;
}