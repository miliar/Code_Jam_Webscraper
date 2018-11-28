#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <cstdio>
#include <ctime>

using namespace std;


int main(int argc, char **argv){
    freopen("/Users/Arseniy/All/Int/input.txt", "r", stdin);
    freopen("/Users/Arseniy/All/Int/int/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ": ";
        int x, r, c;
        cin >> x >> r >> c;
        if ((r*c % x != 0) || (max(r, c) < x) || ((min(r,c) == 1) && (x > 2)) || (x > r+c-1) || (x >= 7) || (x >= 2*min(r,c) +1)){
            cout << "RICHARD" << endl;
            continue;
        }
        if (x <= 3){
            cout << "GABRIEL" << endl;
        }
        if (x == 4){
            if (min(r, c) == 2)
                cout << "RICHARD" << endl;
            else
                cout << "GABRIEL" << endl;
        }
        if (x == 5){
            if ((min(r, c) == 3) && (max(r,c) == 5))
                cout << "RICHARD" << endl;
            else
                cout << "GABRIEL" << endl;
        }
        if (x == 6){
            if (min(r, c) == 3)
                cout << "RICHARD" << endl;
            else
                cout << "GABRIEL" << endl;
        }
    }
    
    return 0;
}