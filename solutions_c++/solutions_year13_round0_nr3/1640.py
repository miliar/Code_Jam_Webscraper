/*
    https://code.google.com/codejam/contest/dashboard?c=2270488#s=p2
*/

#include<boost/lexical_cast.hpp>
#include <iostream>
#include <string>
#include <math.h>
#include <vector>

using namespace std;

int main()
{
    int T;
    string number;   
 
    cin >> T;    
    
    vector<long long> palindromes;

    for (long long i = 1; i <= 10000000; i++) {
        number = boost::lexical_cast<string>(i);
        
        bool isPalindrome = true;
        long long len = number.length();
        for (long long k = 0; k <= len / 2; k++) {
            if (number.at(k) != number.at(len - k - 1)) {
                isPalindrome = false;
                break;
            }
        }

        if (isPalindrome) {
            long long square = i * i;
            number = boost::lexical_cast<string>(square);
            len = number.length();
            
            for (long long j = 0; j <= len / 2; j++) {
                if (number.at(j) != number.at(len - j - 1)) {
                    isPalindrome = false;
                    break;
                }
            }
            
            if (isPalindrome) // found a palindrome squre
                palindromes.push_back(square);
        }
    }  

    for (int i = 0; i < T; i++) {
        long long A, B;
        int result = 0;
        
        cin >> A;
        cin >> B;
    
        for (int j = 0; j < palindromes.size(); j++) {
            if (palindromes.at(j) >= A && palindromes.at(j) <= B) 
                result++;
        }
        
        cout << "Case #" << (i + 1) << ": " << result << endl;
    }
   
    return 0;
}
