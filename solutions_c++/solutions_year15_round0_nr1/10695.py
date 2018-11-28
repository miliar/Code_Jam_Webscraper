#include <iostream>

using namespace std;

int main() {
    int sets;
    cin >> sets;
    string input;
    getline(cin, input);

    for (int set = 1; set <= sets; set++) {
        getline(cin, input);
        int max = input[0] - '0';
        int peopleAttending = input[2] - '0';
        int ans = 0;

        for (int i = 1; i <= max; i++) {
           if (i > peopleAttending) {
               ans += i - peopleAttending;
               peopleAttending += i - peopleAttending;
           }
           peopleAttending += input[i + 2] - '0';
        }

        cout << "Case #" << set << ": " << ans << endl;
    }

    return 0;
}
