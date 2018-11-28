#include <iostream>
#include <sstream>

using namespace std;

string solve()
{
    int possibilities[16];
    for (int i = 0; i < 16; i++) possibilities[i] = 0;

    for (int i = 0; i < 2; i++) {
        int R; cin >> R; cin.ignore();
        for (int j = 0; j < 4; j++) {
            string line; getline(cin, line);
            if ((j+1) == R) {
                istringstream ss(line);
                for (int k = 0; k < 4; k++) {
                    int n; ss >> n;
                    possibilities[n-1]++;
                }
            }
        }
    }

    int index = -1, count = 0;
    for (int i = 0; i < 16; i++) {
        if (possibilities[i] == 2) {
            index = i;
            count++;
        }
    }

    if (count >= 2) return "Bad magician!";
    if (count == 0) return "Volunteer cheated!";
    ostringstream oss;
    oss << index + 1;
    return oss.str();
}

int main()
{
    int T; cin >> T; cin.ignore();
    for (int i = 0; i < T; i++) {
        cout << "Case #" << (i+1) << ": " << solve() << endl;
    }
    return 0;
}
