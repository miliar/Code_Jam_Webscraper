#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;

    string pancakeStack;

    int nManeuver;

    bool foward;

    for (int i = 1; i <= T; i++) {
        cin >> pancakeStack;

        nManeuver = 0;
        foward = true;

        for (int j = pancakeStack.size()-1; j >= 0; j--) {
            if ((pancakeStack[j] == '+')^foward) {
                foward = !foward;
                nManeuver++;
            }
        }
        cout << "Case #" << i << ": " << nManeuver << endl;
    }
    return 0;
}
