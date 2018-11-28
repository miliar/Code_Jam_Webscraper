
#include <iostream>

using namespace std;

int main() {
    int testCases;
    string letters;
    cin >> testCases;
    for(int i = 1; i <= testCases; i++) {
        cin >> letters;
        string word;
        word += letters[0];
        for(unsigned int j = 1; j < letters.length(); j++) {
            if(letters[j] >= word[0]) {
                word = letters[j] + word;
            } else {
                word = word + letters[j];
            }
        }
        cout << "Case #" << i << ": " << word << endl;
    }
    return 0;
}
