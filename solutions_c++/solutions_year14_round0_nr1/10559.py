//
//  codejam.cpp
//  
//
//  Created by Ari Cohen on 4/12/14.
//
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

vector<vector<int> > get_setup() {
    vector<vector<int> > setup;
    vector<int> holder(4);
    for (int y=0; y<4; y++) {
        for (int z=0; z<4; z++) {
            cin >> holder.at(z);
        }
        setup.push_back(holder);
    }
    return setup;
}

int main() {
    ofstream myfile;
    myfile.open ("output.txt");
    int num_cases;
    cin >> num_cases;
    for (int x = 0; x < num_cases; x++) {
        int r1, r2;
        vector<vector<int> > setup;
        vector<int> holder(4), probs1(4), probs2(4);
        cin >> r1;
        probs1 = get_setup().at(r1-1);
        cin >> r2;
        probs2 = get_setup().at(r2-1);
        
        int same = 0, val = 0;
        for (int y=0; y<4; y++) {
            if(find(probs2.begin(), probs2.end(), probs1.at(y))!=probs2.end()) same++, val = probs1.at(y);
        }
        myfile << "Case #" << x + 1 << ": ";
        if (same == 1) {
            myfile << val << endl;
        } else if (same > 1) {
            myfile << "Bad magician!" << endl;
        } else if (same == 0) {
            myfile << "Volunteer cheated!" << endl;
        }
    }
    myfile.close();
    return 0;
}