#include<iostream>
#include<string>
using namespace std;

int main() {
    int t;
    cin >> t;
    for(int i=0; i<t; i++) {
        string ps;
        cin >> ps;
        int flips = 0;
        for (int j=0, k = 1; k < ps.size(); j++,k++) {
            if (ps[j] != ps[k]) {
                flips++;
            }
        }
        if (ps[ps.size()-1] == '-') {
            flips++;
        }
        cout << "Case #" << i + 1 << ": " << flips << endl;
    }
}
