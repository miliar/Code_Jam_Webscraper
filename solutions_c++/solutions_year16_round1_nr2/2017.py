#include <iostream>
#include <string>

using namespace std;

void rankFile(int n) {
    int height[2500];
    for (int i=0; i<2500; i++)
        height[i] = 0;

    int temp;
    for (int i=0; i<2*n-1; i++) {
        for (int j=0; j<n; j++) {
            cin >> temp;
            height[temp-1]++;
        }
    }

    temp = 0;
    for (int i=0; i<2500; i++)
        if (height[i]%2 == 1) {
            temp++;
            cout << i+1;
            if (temp == n) {
                cout << endl; return;
            }
            else
                cout << " ";
        }

}

int main() {
    int t; int n;
    cin >> t;
    for (int i=0; i<t; i++) {
        cin >> n;
        cout << "Case #" << i+1 << ": "; rankFile(n);
    }
    return 0;
}
