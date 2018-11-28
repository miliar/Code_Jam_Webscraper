#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    for (int ca = 0; ca < T; ++ca) {
        int s_max;
        cin >> s_max;

        int min = 0;
        int count = 0;
        for (int i = 0; i < s_max + 1; ++i) {
            char c;
            int current;
            cin >> c;
            current = c - '0';

            if (count >= i)
                count += current;
            else {
                min += (i - count);
                count += current + (i - count);
            }
        }
        cout << "Case #" << ca+1 << ": " << min << endl;
    }

}
