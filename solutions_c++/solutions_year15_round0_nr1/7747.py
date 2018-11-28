#include <iostream>
using namespace std;

void solveTest() {
    int shynessLevel;
    int people[1002] = {};
    char pe[1002] = {};
    cin >> shynessLevel;
    cin >> pe;
    for(int i=0; i<=shynessLevel; i++) {
        people[i] = pe[i] - '0';
    }

    int required = 0;
    int total = 0;
    total += people[0];
    for(int i=1; i<=shynessLevel; i++) {
        if(people[i]!=0) {
            if(i <= total) total += people[i];
            else {
                int added = i-total;
                required += added;
                total += added;
                total += people[i];
            }
        }
    }
    cout << required;
}


int main() {
    int T;
    cin >> T;
    for(int i=0; i<T; i++) {
        cout << "Case #" << i+1 << ": ";
        solveTest();
        cout << "\n";
    }

}
