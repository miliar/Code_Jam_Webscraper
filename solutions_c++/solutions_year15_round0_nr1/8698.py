#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>

using namespace std;
static const int DEBUG = 0;
static const int PROBLEM = 1; //Small=1, Large = 2;

int solve(vector<int> members) {
    
    int totalAdditional = 0;
    int standing = 0;
    int additional = 0;

    for (int s=0; s < members.size(); s++) {

        if (members[s] == 0) continue;
        
        if (standing >= s) {

            standing += members[s];
            if (DEBUG) cout << standing << " people are standing" << endl;
        } 
        else {

            additional = s - standing;
            standing += members[s] + additional;
            if (DEBUG) cout << standing << " people are standing." << additional <<
                " people were added" << endl;
            totalAdditional += additional;
        }
    }

    return totalAdditional;
}

int main(void) {
    /* number of test cases */
    unsigned short int testcases;
    int Smax;
    vector<int> members;    
    
    char members_num;
    
    // Read number of testcases
    cin >> testcases;


    // For each testcase
    for(int i=1; i <= testcases; i++) { //loops for each case
        
        cin >> Smax;
        members.resize(Smax + 1);

        for (int s=0; s <= Smax; s++) {

            fscanf(stdin," %c",&members_num);
            members[s] = members_num - '0';
            if (DEBUG) { cout << "# of Members With Shyness Level " << s << 
                " : " << members[s] << endl; }
        }

        cout << "Case #" << i << ": " << solve(members) << endl;
    }

    return 0;
}