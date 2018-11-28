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
        bool digits[10] = {};
        int N;
        cin >> N;

        if(N == 0){
            cout << "Case #" << k + 1 << ": INSOMNIA" << endl;
            continue;
        }

        int i = 1;

        while(true){

            string str = to_string(N * i);
            for(int i = 0; i < str.size(); i++){
                digits[str[i] - '0']++;
            }

            bool allSeen = true;
            for(int i = 0; i < 10; i++){
                if(!digits[i]){
                    allSeen = false;
                    break;
                }
            }

            if(allSeen){
                cout << "Case #" << k + 1 << ": " << N * i << endl;
                break;
            }

            i++;
        }
    }

    return 0;
}

