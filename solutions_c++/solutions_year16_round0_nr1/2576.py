#include <algorithm>
#include <iostream>
#include <set>
using namespace std;

int main() {

    int cases;
    cin >> cases;

    for( int i = 0; i < cases; i++) {
        set<int> numbers;
        int N;
        cin >> N;

        if (N == 0) {
            cout << "Case #" << (i + 1) << ": " << "INSOMNIA" << endl;
            continue;
        }
        int mul = 1;
        while(1) {
            int temp = N * mul;
            int out = temp;
            while(temp > 0) {
                numbers.insert(temp%10);
                temp /= 10;
            }
            mul++;
            if(numbers.size() == 10) {
                cout << "Case #" << (i + 1) << ": " << out << endl;
                break;
            }
        }
    }


}
