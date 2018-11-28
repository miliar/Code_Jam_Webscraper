#include <iostream>
#include <cmath>
#include <sstream>
#include <string>


using namespace std;

bool isPalindrome(int num) {
     stringstream ss;
     string str;
     ss << num;
     str = ss.str();

     int size = str.size();
     for (int i = 0; i <= size - i - 1; i++) if (str[i] != str[size - i - 1]) return false;

     return true;
}

int main() {
    int T,A,B,result;
    
    cin >>T;
    
    for (int i =1; i <= T; i++) {
        cin >>A >>B;
        result = 0;
        
        float sqA = sqrt(A);
        int start = (int) sqA;
        if (sqA - start != 0.0f) start++;
        while (start*start <= B) {
              if (isPalindrome(start) && isPalindrome(start*start)) result++;
              start++;
        }
        
       cout <<"Case #" <<i <<": " <<result <<endl;
    }
}

