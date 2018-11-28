#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>
using namespace std;

int main() {
    int t;
    cin >> t;
    int answer[t];
    for (int i=0;i<t;i++) {
        string n;
        cin >> n;
        int len = n.length(); int flip = 0;
        for (int j=0;j<(len-1);j++) {
            if ((n.substr(j,1)) != (n.substr(j+1,1))) {
               flip++;
            }
        }
        if (n.substr(len-1,1)=="-") {
           flip++;
        }
        answer[i] = flip;
    }
    for (int i=0;i<t;i++) {
        cout << "Case #" << i+1 << ": " << answer[i] << endl;
    }
    return 0;
}
