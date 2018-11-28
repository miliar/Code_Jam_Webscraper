#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int master = 0; master < cases; master++) {
        cout << "Case #" << master + 1 << ": ";
        int maxshy;
        string people;
        cin >> maxshy >> people;
        int ans = 0;
        int standing = 0;
        for (int i = 0; i < people.size(); i++) {
            //cout << people[i] << "\n";
            int numpeople = people[i] - '0';
            //cout << numpeople << "\n";
            if (standing >= i) {
                standing += numpeople;
            } else {
                ans += i - standing;
                standing += numpeople + i - standing;
            }
        }
        cout << ans << "\n";
    }
}