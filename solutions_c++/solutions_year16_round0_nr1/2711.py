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

int countSheep(int i) {
    if(i == 0) return 0;
    set<int> count;
    int k = 1;
    while(1) {
        int num = i*k;
        while(num > 0) {
            count.insert(num%10);
            num/=10;
        }
        if(count.size() == 10) {
            return i*k;
        }
        k++;
    }
}

int main() {
    
    ifstream inf("/Users/Hiukin/A-small-attempt0.in");
    
    char buffer[256];
    inf.getline(buffer, 256);
    int casenum = stoi(buffer);
    
    for(int i=1; i<=casenum; i++) {
        inf.getline(buffer, 256);
        int num = stoi(buffer);
        int res = countSheep(num);
        if(res != 0) {
            cout << "Case #" << i << ": " << res << endl;
        } else {
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }
    }
    
    return 0;
}
