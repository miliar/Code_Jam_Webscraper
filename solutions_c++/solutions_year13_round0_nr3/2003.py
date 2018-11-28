#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

int digits[20];
vector<long long> palindromes;

int isPalindrome(long long num) {
    int numDigits = 0;
    if (num % 10 == 0) return false; // no leading zeros
    while (num > 0) {
          digits[numDigits] = num % 10;
          num = num / 10;
          numDigits++;
    } 
    for (int i = 0; i < numDigits; i++) {
        if (digits[i] != digits[numDigits-1-i]) return false;        
    }    
    return true;
}
     
int doit(long long themin, long long themax) {
     long long count = 0;
     for (int i = 0; i < palindromes.size(); i++) {
         if (palindromes[i] >= themin && palindromes[i] <= themax) count++;
     }
     return count;
}

int main() {
    
    // a little more than 10^7
    for (long long i = 0; i < 11000000; i++) {
        if (!isPalindrome(i)) continue;
        long long square = i*i;
        if (!isPalindrome(square)) continue;
        palindromes.push_back(square);     
    }
    
    ifstream infile("C:/a.in");
    ofstream outfile("C:/a.out");
    int numCases = 0;
    infile >> numCases;
    for (int i = 0; i < numCases; i++) {
        long long themin, themax;
        infile >> themin >> themax;
        long long count = doit(themin, themax);
        outfile << "Case #" << (i+1) << ": " << count << endl;
    }    
    outfile.close();
    //system("PAUSE");
    return 0;
    
}
