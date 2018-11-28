/*Code written for Google CodeJam by Dylan Jeffers 4/11/15
License: GPLv3
*/
#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    int max, friends, clappers;
    string peopleList;
    for (int i=0; i<cases; i++) {
        cin >> max >> peopleList;
        clappers = friends = 0;
        for (int j=0; j<=max; j++) {
            if (clappers >= j) {
                clappers += (peopleList[j] - '0');
            }
            else {
                int disparity = (j - clappers);
                friends += disparity;
                clappers += disparity + (peopleList[j] - '0');
            }
        }
        cout << "Case #" << i+1 << ": " << friends << endl;
    }
    return 0;
}
