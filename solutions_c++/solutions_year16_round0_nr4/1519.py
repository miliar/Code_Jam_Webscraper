#include <iostream>
#include <string>
using namespace std;

int main() {

    int t, k, c, s;
    cin >> t;
    for (int test=1; test<=t; test++) {
        cin >> k >> c >> s;
        cout << "Case #" << test << ":";
        for (int i=0; i<s; i++)
            cout << " " << i+1 ;
        cout << endl;
    }
}
