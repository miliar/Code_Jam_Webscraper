#include <iostream>

using namespace std;

int main() {
    bool arr[17];
    int T, ans, read, count, pos;
    cin >> T;

    for(int cas = 1; cas <= T; cas++) {
        fill(arr, arr+17, false);
        count = 0;
        cin >> ans;
        for(int ix = 1; ix <= 4; ix++) {
            for(int iy = 0; iy < 4; iy++) {
                cin >> read;
                if(ans == ix)
                    arr[read] = true;
            }
        }

        cin >> ans;
        for(int ix = 1; ix <= 4; ix++) {
            for(int iy = 0; iy < 4; iy++) {
                cin >> read;
                if(ans == ix && arr[read]) {
                    count++; 
                    pos = read; 
                }
            }
        }

        if(count == 0)
            cout << "Case #" << cas << ": Volunteer cheated!" << endl;
        else if(count > 1)
            cout << "Case #" << cas << ": Bad magician!" << endl;
        else
            cout << "Case #" << cas << ": " << pos << endl;
    }

    return 0;
}
