#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <iterator>
#include <map>
#include <queue>
#include <stack>
#include <utility>
using namespace std;

template<typename T>
std::string to_string(T input) {
        std::ostringstream s;
            s << input;
                return s.str();
}

template<typename T>
T from_string(const std::string& str) {
        T output;
            std::istringstream s(str);
                s >> output;
                    return output;
}


int main() {
    long T;
    cin >> T;
    for (long i = 1 ; i <= T; i++) {
        long size, other;        
        cin >> size >> other;

        vector<long> motes;
        for (long j = 0; j < other; j++) {
            long temp;
            cin >> temp;
            motes.push_back(temp);
        }
        if (size == 1) {
            cout << "Case #" << i << ": "<<other<<endl;
            continue;
        }
        sort(motes.begin(), motes.end());
        long currentSize = size;
        long operations = 0;
        long consumed = 0;
        vector<long> operationList;
        for (int k = 0; k < other; k++)
            operationList.push_back(0);
        for (int k = 0; k < other; k++) {
            if (currentSize > motes[k]) {
                currentSize += motes[k];
                operationList[k] = operations;
            } else {
                while (currentSize <= motes[k]) {
                    currentSize = 2*currentSize - 1;
                    operations++;
                }
                currentSize = currentSize + motes[k];
                operationList[k] = operations;
            }            
        }
        int minimum = other;
        for (int k = 0; k < other; k++) {
            int temp = operationList[k] + other - (k+1);
            if (minimum > temp)
                minimum = temp;
        }        
        cout << "Case #" << i << ": "<<minimum<<endl;
        operationList.clear();
        motes.clear();
    }
}





