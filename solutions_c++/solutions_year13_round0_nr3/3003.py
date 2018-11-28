#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

bool isPalindrome(int);

int main( void ) {
    vector < int > listOfFS;
    int t;
    cin >> t;
    for(int curNum = 1; curNum*curNum < 1000; ++curNum)
            if(isPalindrome(curNum) && isPalindrome(curNum*curNum)) {
                listOfFS.push_back(curNum*curNum);
            }
    for(int k = 0; k < t; ++k) {
        int a, b, numFS = 0;
        cin >> a >> b;
        for(int i = 0; i < listOfFS.size(); ++i){
          if(listOfFS.at(i) >= a && listOfFS.at(i) <= b)
                ++numFS;
        }
        cout << "Case #" << k + 1<< ": " << numFS << endl;
    }
    return 0;
}

bool isPalindrome(int i) {
    char intStr[10];
    itoa(i, intStr, 10);
    string s = string(intStr);
    if( equal(s.begin(), s.begin() + s.size()/2, s.rbegin()) )
        return true;
    return false;
}
