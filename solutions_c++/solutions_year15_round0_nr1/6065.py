#include <iostream>
#include <string>
using namespace std;

int main(int argc, char **args) {
    int num_cases;
    cin >> num_cases;

    for(int case_num=0; case_num < num_cases; case_num++) {
        int max_shy;
        string input_string;
        cin >> max_shy >> input_string;

        // Just find how many people have risen for each step, and invite however many we need
        int added = 0, standing=0;
        for(int i=0; i < input_string.length(); i++) {
            int num_here = (int)(input_string[i])-48;
            if(num_here == 0) continue;
            if(i > standing) {
                added += i - standing;
                standing += i - standing;
            }
            standing += num_here;
        }

        cout << "Case #" << case_num+1 << ": " << added << endl;
    }

    return 0;
}
