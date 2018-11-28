#include <iostream>
#include <string>
using namespace std;
void print(bool arr[], int size);
void flip(bool arr[], int size, int n);
int find(bool arr[], int size);

int main() {
    string input;
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; ++i) {
        cin >> input;
        int size = input.length();
        bool arr[size];
        for (int j = 0; j < size; ++j)
            arr[j] = input[j] == '+' ? 1 : 0;

        int flipcount = 0;
        bool saw = false;

        for (int j = 0; j < size; ++j) {
            if (saw && arr[j] == 0)
                continue;
            else if (!saw && arr[j] == 0) {
                flipcount += 2;
                saw = true;
            }
            else if (saw && arr[j] == 1)
                saw = false;
        }
        if (arr[0] == 0)
            flipcount--;
        cout << "Case #" << i << ": " << flipcount << '\n';
    }
}
