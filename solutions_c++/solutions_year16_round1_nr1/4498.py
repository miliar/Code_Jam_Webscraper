#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <math.h>
#include <sstream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
//#include <algorithm>
using namespace std;


int main() {
    
    
    ifstream inf("/Users/Hiukin/GoogleCodeJam/1a/A-small-attempt0.in");
    
    char buffer[256];
    inf.getline(buffer, 256);
    int casenum = stoi(buffer);

    for(int i=1; i<=casenum; i++) {
        inf.getline(buffer, 256);
        string str = buffer;
        string res = str.substr(0, 1);
        for(int i=1; i<str.length(); i++) {
            if(str[i] < res[0]) {
                res = res + str[i];
            } else {
                res = str[i] + res;
            }
        }
        
        
        cout << "Case #" << i << ": " << res << endl;
    }
    
    return 0;
}