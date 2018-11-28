#include <cassert>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <gmpxx.h>
#include <Audience.hpp>
using namespace std;


//------------------------------------------------------------------------------
int main() {
    int caseCount;
    cin >> caseCount;
    //    cout << "caseCount: " << caseCount << endl;

    Audience audience;
    for (int i = 1; i <= caseCount; ++i) {
        audience.init();
        audience.calc();
        //        audience.dump();
        cout << "Case #" << i << ": " << audience.friendCount() << endl;
    }
    
    return 0;
}

//------------------------------------------------------------------------------
