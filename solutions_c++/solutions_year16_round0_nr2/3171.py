#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int round = 1; round <= t; ++round) {
        string input;
        cin >> input;
        int ret = 0;

        int last = input.size() - 1;

        while(true) {
            int i;
            for(i = last; i >= 0; i--) {
                if (input[i] == '-')
                    break;
            }

            // Completed
            if (i == -1) break;

            last = i;

            if (input[0] == '+') {
                int anchor = last;

                for (int j = 1; j < last; ++j) {
                   if (input[j] == '-') {
                       anchor = j;
                       break;
                   }
                }
                ret++;
                reverse(input.begin(), input.begin() + anchor - 1);
                for(int j = 0; j < anchor; ++j) {
                    input[j] = '-';
                }
            }

            ret++;
            reverse(input.begin(), input.begin() + last + 1);
            for(int j = 0; j < last + 1; ++j) {
                switch(input[j]){
                    case '-':
                        input[j] = '+';
                        break;
                    case '+':
                        input[j] = '-';
                        break;
                }
            }
        }
        cout << "Case #" << round << ": " << ret << endl;
    
    }
    return 0;
}
