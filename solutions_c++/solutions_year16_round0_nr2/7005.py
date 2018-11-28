#include <iostream>
using namespace std;

int flips(string pancakes) {
    int num = 0;
    bool bottom = true;
    for (int i = pancakes.size() - 1; i >= 0; --i) {
        if (bottom && pancakes[i] == '+') {
            continue;
        } else bottom = false;
        if (i == pancakes.size()) {
            num++;
            continue;
        }
        if (pancakes[i] != pancakes[i+1]) num++;
    }
    return num;
}

int main(int argc, char const *argv[])
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string pancakes;
        cin >> pancakes;
        cout << "Case #" << i+1 << ": " << flips(pancakes) << endl;
    }
    return 0;
}