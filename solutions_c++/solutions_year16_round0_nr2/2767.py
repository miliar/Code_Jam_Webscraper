#include <iostream>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <math.h>
#include <sstream>
#include <fstream>
#include <unordered_map>
#include <string>
#include <stack>
#include <unordered_map>
#include <unordered_set>
//#include <algorithm>
using namespace std;


int main() {
    
    ifstream inf("/Users/Hiukin/GoogleCodeJam/B-small-attempt0.in");
    
    char buffer[256];
    inf.getline(buffer, 256);
    int casenum = stoi(buffer);
    
    for(int i=1; i<=casenum; i++) {
        inf.getline(buffer, 256);
        string str = buffer;
        int count = 0;
        
        for(int i=0; i<str.length(); i++) {
            while(i+1<str.length() && str[i+1] == str[i]) {
                i++;
            }
            if(i != str.length()-1 || str[str.length()-1] != '+') {
                count++;
            }
        }
        
        cout << "Case #" << i << ": " << count << endl;
    }
    
    return 0;
}
