#include <cstdio>
#include <iostream>
#include <string>
//#include <fstream>
using namespace std;

bool fits(int x, int r, int c);

int main() {
    int t,x,r,c,i, caseNumber = 1;
    cin >> t;
    for(i=0;i<t;i++) {
        cin >> x;
        cin >> r;
        cin >> c;
        if(fits(x,r,c))
            cout << "Case #" << caseNumber++ << ": GABRIEL" << endl;
        else 
            cout << "Case #" << caseNumber++ << ": RICHARD" << endl;
    }
    return 0;
}

bool fits(int x, int r, int c) {
    int area = r*c;
    //cout << "R: " << r << " C: " << c << endl;
    if(x == 1){
        return true;
    }
    else if(x == 2) {
        if(area % x == 0)
            return true;
        else 
            return false;
    }
    else if(x == 3) {
        if((area % x == 0) && ((r >= 2) && (c >=2)))
            return true;
        else
            return false;
    } 
    else if((x == 4) && (((r >= 4) && (c >2)) || ((r > 2) && (c >=4)))) {
        if(area % x == 0)
            return true;
        else 
            return false;
    }
    return false;
}