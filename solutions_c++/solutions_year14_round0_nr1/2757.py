#include <cstdlib>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main(int argc, char** argv) {

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int T, a1, a2, c1[4][4], c2[4][4];
    
    cin >> T;

    for (int k = 1; k <= T; k++) {
        vector <int> v(8);
        vector <int>::iterator it;
        cin >> a1;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> c1[i][j];
            }
        }
        cin >> a2;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> c2[i][j];
            }
        }
        a1--;
        a2--;
        
        sort(c1[a1], c1[a1]+4);
        sort(c2[a2], c2[a2]+4);
        
        it = set_intersection(c1[a1], c1[a1] + 4, c2[a2], c2[a2] + 4, v.begin());
        v.resize(it - v.begin());
        
        cout << "Case #" << k << ": ";
        if(v.size() == 1){
            cout << *(v.begin());
        } else if(v.size() == 0){
            cout << "Volunteer cheated!";
        } else {
            cout << "Bad magician!";
        }
        cout << endl;
    }

    return 0;
}

