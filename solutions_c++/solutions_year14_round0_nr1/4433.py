#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_set>

using namespace std;

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
    
    const int R = 4; // number of cards in one row
    
    int N; // number of cases
    input >> N;
    input.ignore(256, '\n'); // ignore the rest of the line
    
    // consider each case
    for (int i = 1; i <= N; i++) {
        string line;
        unordered_set<int> st; // store all values from the row chosen at the first time
        int rowID; // row ID for chosen card
        // deal with the first arrangment
        input >> rowID; // row ID for first time
        input.ignore(256, '\n'); // ignore the rest of the line
        
        for (int j = 1; j <= R; j++) {
            getline(input, line); // get one line
            if (j != rowID) continue; // only consider the chosen row
            stringstream ss(line);
            for (int index = 1; index <= R; index++) {
                int x;
                ss >> x;
                if (st.count(x) == 0) st.insert(x); // add all unique value of the chosen row into the set
            }
        }
        // deal with the second arrangment
        input >> rowID; // row ID for second time
        input.ignore(256, '\n'); // ignore the rest of the line
        
        int count = 0; // count how many possible cards
        int card = -1; // chosen card if just one, assume -1 can not be a card
        
        for (int j = 1; j <= R; j++) {
            getline(input, line); // get one line
            if (j != rowID) continue; // only consider the chosen row
            stringstream ss(line);
            for (int index = 1; index <= R; index++) {
                int x;
                ss >> x;
                if (st.count(x) != 0) { // if x is possible
                    if (card != x) {
                        card = x;
                        count++;
                        if (count > 1) break;
                    }
                }
            }
        }
        if (count > 1) cout << "Case #" << i << ": Bad magician!" << endl; // multiple choices
        else if (count == 1) cout << "Case #" << i << ": " << card << endl; // unique choice
        else cout << "Case #" << i << ": Volunteer cheated!" << endl; // no choice
    }
    
    
    input.close(); // close file before return
    
    return 0;
}
















