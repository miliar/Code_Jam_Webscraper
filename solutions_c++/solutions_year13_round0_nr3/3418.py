#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

bool isPalindrome(int number);
string intToStr(int num);
void algo(int min, int max);




int main() {
    
    int nCases;
    cin >> nCases;
    
    int minInterval,maxInterval;
    
    for(int i=0;i<nCases;i++) {
        cin >> minInterval;
        cin >> maxInterval;
        
        cout << "Case #" << i+1 << ": ";
        algo(minInterval,maxInterval);
        cout << endl;
    }
 
    return 0;
}

void algo(int min, int max) {
    int minIndex = ceil(sqrt(min));
    int maxIndex = floor(sqrt(max));
    
    int nFairAndSquare=0;
    
    for(int i=minIndex; i <= maxIndex;i++) 
        if(isPalindrome(i)) 
            if(isPalindrome(i*i))
                nFairAndSquare++;
        
    cout << nFairAndSquare;
}

bool isPalindrome(int n) {
    string number = intToStr(n);
    
    string numberInv = string (number.rbegin(), number.rend());
    return numberInv == number;
}

string intToStr(int num)  {
    std::stringstream ss;
    ss << num;
    string str;
    ss >> str;
    return str;
}

