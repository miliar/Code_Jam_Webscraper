#include <stdio.h>
#include <iostream>


using namespace std;

/*
 * @function main
 * @brief Main function
 */
int main(int argc, char **argv) {
    int T;
    cin >> T;

    for(int k = 0; k < T; k++){
        string pancakesStr;
        cin >> pancakesStr;

        while(pancakesStr[pancakesStr.size() - 1] == '+')
            pancakesStr = pancakesStr.substr(0, pancakesStr.size() - 1);

//        cout << pancakesStr << endl;

        int changes = 0;
        int r = 0;

        if(pancakesStr.size()) {
            char last = pancakesStr[0];

            for (int i = 1; i < pancakesStr.size(); i++) {
                if (pancakesStr[i] != last) {
                    changes++;
                }

                last = pancakesStr[i];
            }

            if(pancakesStr[0] == '+'){
                r += 1;
            }
            r = changes + 1;
        }

        cout << "Case #" << k + 1 << ": " << r << endl;
    }

    return 0;
}

