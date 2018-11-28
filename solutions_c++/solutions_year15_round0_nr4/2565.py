#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <cassert>

using namespace std;

bool DEBUG=false;

typedef vector<int> testcase;
typedef vector<testcase> testblock;
typedef vector<char> solutions;

void read_testcases(testblock &T) {
    int num_testcases;
    cin >> num_testcases;
    T.resize(num_testcases);
    for(int i=0; i<num_testcases; ++i) {
        T[i].resize(3);
        for(int j=0; j<3; ++j) {
            cin >> T[i][j];
        }
    }
}

void print_testcases(testblock &T, solutions &S) {
    if (DEBUG)
        for(int i=0; i<T.size(); ++i) {
            cout << "testcase " << i+1 << ": ";
            for(int j=0; j<T[i].size(); ++j) {
                cout << T[i][j] << " ";
            }
            cout << endl;
            cout << "  solution: " << S[i] << endl;
        }
}

void print_solutions(solutions &S) {
    for(int i=0; i<S.size(); ++i) {
        cout << "Case #" << i+1 << ": " << ((S[i]=='G') ? "GABRIEL" : "RICHARD") << endl;
        //assert(S[i] != '0');        
        //cout << "Case #" << i+1 << ": " << S[i] << endl;
    }
}
    

void solve(testblock &T, solutions &S) {
    for(int i=0; i<T.size(); ++i) {
        int X, R, C;

        X = T[i][0];
        R = T[i][1];
        C = T[i][2];

        int min_board = min(R, C);
        int max_board = max(R, C);

        //construct 'L' shape dimensions
        int max_short_omino = (X-1)/2 + 1;
        int min_long_omino = X - (max_short_omino - 1);

        if (X >= 7) { //can choose N-omino with hole
            S[i] = 'R'; 
        } else if (((R*C) % X) != 0) { //does not fit
            S[i] = 'R';
        } else if (X > max(R, C)) { //choose 'stick'
            S[i] = 'R';
        } else if (max_short_omino > min_board){ //choose 'L'
            S[i] = 'R';
        } else if ((max_short_omino == min_board)){ //can we force bad partitioning?
            bool match_found = false;
            bool position_without_match = false;
            for(int m=1; m <= (min_long_omino-1)/2; ++m) { //slide 'nose' along 'base'
                match_found = false;
//                cout << "testing m=" << m << endl;
                for(int n=0; n<max_board-min_long_omino; ++n) { //slide omino along max axis
//                    cout << "testing match: m=" << m << ", n=" << n << endl;
                    if ((n*min_board+m*(min_board-1)) % X == 0 ) {
                        match_found = true;
                        break;
                    }
                }
                if (!match_found) {
                    position_without_match = true;
                    break;
                }
            }
            if (position_without_match) {
                S[i] = 'R';
            } else {
                S[i] = 'G';
            }
        } else {
            S[i] = 'G';
        }
    }
}
            

int main(int argc, char** argv) {
    testblock T;
    solutions S;
    read_testcases(T);
    S.resize(T.size(), '0');

    testblock T_orig(T);
    
    solve(T, S);
    
    print_testcases(T_orig, S);

    print_solutions(S);

    return 0;
}
