#include <iostream>
#include <set>

using namespace std;

int main() {

    int t = 0, f, s, num, oldSize, currentSize;
    int input[3500];
    set<int> nums;

    while (cin >> input[t]) {
        t++;
    }

    t = input[0];
    for (int i=0; i<t; i++) {

        f = 1 + (i*17*2);
        s = 18 + (i*17*2);
        
        
        nums.insert(input[((input[f]-1)*4)+f+1]);
        nums.insert(input[((input[f]-1)*4)+f+2]);
        nums.insert(input[((input[f]-1)*4)+f+3]);
        nums.insert(input[((input[f]-1)*4)+f+4]);

        oldSize = nums.size();
        nums.insert(input[((input[s]-1)*4)+s+1]);
        currentSize = nums.size();
        if (oldSize == currentSize) {
            num = input[((input[s]-1)*4)+s+1];
        }
        oldSize = currentSize;
        nums.insert(input[((input[s]-1)*4)+s+2]);
        currentSize = nums.size();
        if (oldSize == currentSize) {
            num = input[((input[s]-1)*4)+s+2];
        }
        oldSize = currentSize;
        nums.insert(input[((input[s]-1)*4)+s+3]);
        currentSize = nums.size();
        if (oldSize == currentSize) {
            num = input[((input[s]-1)*4)+s+3];
        }
        oldSize = currentSize;
        nums.insert(input[((input[s]-1)*4)+s+4]);
        currentSize = nums.size();
        if (oldSize == currentSize) {
            num = input[((input[s]-1)*4)+s+4];
        }

        if (nums.size() == 8) {
            cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
        } else if (nums.size() == 7) {
            cout << "Case #" << i+1 << ": " << num << endl;
        } else {
            cout << "Case #" << i+1 << ": Bad magician!" << endl;
        }
        nums.clear();
    }

    return 0;
}
