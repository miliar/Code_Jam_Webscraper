#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

string solve();

int main(void) {

    unsigned short int testcases;           // number of input test cases
    cin >> testcases;

    char *shyguys_atlevel = NULL;

    for(int i=1; i <= testcases; i++) {     // loops for each case

        unsigned short int shy_max;
        cin >> shy_max;

        if (shyguys_atlevel!=NULL) delete shyguys_atlevel;
        shyguys_atlevel = new char[shy_max+2];
        cin >> shyguys_atlevel;

        int needs = 0;
        int standers = 0;
        int shyguys_atl;
        for (int i=0; i<shy_max+1; i++) {
            shyguys_atl =shyguys_atlevel[i] - '0';

            if (standers<i) {
                needs += i-standers;
                standers = i;
            }
            standers = standers+shyguys_atl;
        }
        cout << "Case #" << i << ": " << needs << endl;

    }

    return 0;
}

string solve() {
    return "solved.";
}

