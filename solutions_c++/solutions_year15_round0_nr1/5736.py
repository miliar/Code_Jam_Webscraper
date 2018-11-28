#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

bool DEBUG=false;

typedef vector<int> testcase;
typedef vector<testcase> testblock;
typedef vector<int> solutions;

void read_testcases(testblock &T) {
    int num_testcases;
    cin >> num_testcases;
    if (DEBUG)
        cerr << "num testcases: " << num_testcases << endl;
    T.resize(num_testcases);
    for(int i=0; i<num_testcases; ++i) {
        int S_max;
        string Sbuf;
        cin >> S_max >> Sbuf;
        T[i].resize(S_max+1);
        for(int j=0; j<S_max+1; ++j) {
            char a = Sbuf[j];
            T[i][j] = atoi(&a);
        }
    }
}

void print_testcases(testblock &T) {
    for(int i=0; i<T.size(); ++i) {
        cout << "i=" << i << " ";
        for(int j=0; j<T[i].size(); ++j) {
            cout << T[i][j] << " ";
        }
        cout << endl;
    }
}

void print_solutions(solutions &S) {
    for(int i=0; i<S.size(); ++i) {
        cout << "Case #" << i+1 << ": " << S[i] << endl;
    }
}
    

void solve(testblock &T, solutions &S) {
    for(int i=0; i<T.size(); ++i) {
        int invitedFriends = 0;
        int standing = 0;

        for(int j=0; j<T[i].size(); ++j) {
            if (standing < j) {
                invitedFriends += j-standing;
                standing += j-standing;
                }
            standing += T[i][j];
        }
        S[i] = invitedFriends;
    }
}
            

int main(int argc, char** argv) {
    testblock T;
    solutions S;
    read_testcases(T);
    S.resize(T.size(), -1);

    solve(T, S);

    if (DEBUG)
        print_testcases(T);

    print_solutions(S);

    return 0;
}
