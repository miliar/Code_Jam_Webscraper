#include <iostream>
#include <ctype.h>
#include <assert.h>

using namespace std;

int solve(int);

int main(){
    int no_cases = 0;
    cin >> no_cases;

    //read and process each case
    for(int i = 0; i < no_cases; i++){
        int s_max;
        cin >> s_max;
        //cerr << "================================================================================\n";
        cout << "Case #" << i + 1 << ": " << solve(s_max + 1) << "\n";
    } //end for

    return 0;
}

/** Determines the no. of people who must be added to effect a standing ovation.
 * Values are read from stdin
 * N: the no. of values/chars to be read from stdin
 */
int solve(int N){
    int sum = 0;
    int added = 0;
    char c;

    for(int i = 0; i < N; i++){
        cin >> c;
        //cerr << "Processing: '" << c << "'\n";
        assert(isdigit(c));
        c -= '0';

        if(sum < i){
            added += i - sum;
            sum = i;
        } //end if

        sum += c;

    } //end for

    return added;
}


