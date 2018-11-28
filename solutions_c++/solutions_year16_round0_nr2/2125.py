#include <iostream>

using namespace std;

int main() {
    int T = 0;
    cin >> T;
    char buff[101];
    cin.getline(buff, 101);
    for (int i=1; i<=T; ++i) {
        cin.getline(buff, 101);
        int numAlternations = 0;
        char lastChar = 0;
        for(int j = 0; buff[j] != '\0'; ++j){
            if((lastChar == '+' && buff[j] == '-')||
               (lastChar == '-' && buff[j] == '+')){
                ++numAlternations;
            }
            if(buff[j] == '+' || buff[j] == '-'){
                lastChar = buff[j];
            }
        }
        if(lastChar == '-'){
            ++numAlternations;
        }

        cout << "Case #" << i << ": " << numAlternations << endl;
    }

    return 0;
}