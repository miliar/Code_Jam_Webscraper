#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    long T, Smax;
    string shynesses;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> Smax;
        cin >> shynesses;
        vector<int> students;
        for (int i = 0; i <= Smax; i++) {
            for (int j = 0; j < shynesses[i] - '0'; j++) {
                students.push_back(i);
            }
        }
        int needed = 0;
        for (int i = 0; i < students.size(); i++) {
            needed = max(needed, students[i] - i);
        }
        cout << "Case #" << t << ": " << needed << endl;
    }
}
