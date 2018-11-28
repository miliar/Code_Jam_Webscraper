#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int func(int orig) {
    set<int> x;
    set<int> numbers;
    for (int i = 0; i <= 9; i++) {
        numbers.insert(i);
    }
    bool isINSOMNIA = false;
    int count = 0;
    int n;

    do {
        n = (++count) * orig;
        // if number is already visited
        if (x.count(n) > 0) {
            isINSOMNIA = true;
            break;
        } else {
            int temp = n;
            x.insert(temp);
            while (temp) {
                if (numbers.count(temp%10) > 0) {
                    numbers.erase(temp%10);
                }
                temp /= 10;
            }
        }
    } while (numbers.size() > 0);

    if (isINSOMNIA) {
        return 0;
    }
    return n;
}
int main() {
    ofstream myfile;
    myfile.open ("output.txt");
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int n;
        cin >> n;
        int result = func(n);
        if (result == 0) {
            myfile << "Case #" << i << ": INSOMNIA " << endl;
        } else {
            myfile << "Case #" << i << ": " << result << endl;
        }
    }
    myfile.close();
    return 0;
}
