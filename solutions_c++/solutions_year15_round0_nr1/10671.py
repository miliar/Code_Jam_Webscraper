#include "iostream"
#include "string"

using namespace std;

int main() {
    int T, n, i, maxS, standings, needs;
    
    cin >> T;
    for (int test_number = 0; test_number < T; test_number++) {
        cin >> maxS;
        char Shyness[maxS+1];
        cin >> Shyness;
        standings = (int)(Shyness[0] - '0');
        needs = 0;
        for (i = 1; i < maxS+1; i++) {
            if (standings >= i) {
                standings += (int)(Shyness[i] - '0');
            }
            else if ((int)(Shyness[i] - '0') != 0){
                needs += i - standings;
                standings += i - standings + (int)(Shyness[i] - '0');
            }
        }
        cout << "Case #" << test_number+1 << ": " << needs << endl;
    }
    return 0;
}