#include <iostream>
#include <string>

using namespace std;

int main() {
    int rounds;
    cin >> rounds;

    for (int round = 1; round < rounds + 1; round++) {
        string letters;
        string word;

        cin >> letters;

        for (char c : letters) {
            c = toupper(c);
            if (word.length() == 0) {
                word = string(1, c);

                continue;
            }

            if (int(c) < int(word[0])) {
                word += c;
            } else {
                word = c + word;
            }
        }

        cout << "Case #" << round << ": " << word << endl;
    }

    return 0;
}