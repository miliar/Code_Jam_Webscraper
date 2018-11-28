#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

ofstream fout("output.txt");

static int testCase, N, J, nJamcoins; /* N: length of jamcoin, J: the number of diff jamcoins */

int isPrime(long number)
{
    int threshold = sqrt(number);
    
    for (int i = 2; i <= threshold; i++)
        if (number % i == 0) return i;
    return -1;
}

void isJamcoin(string digits)
{
    long number;
    int divisor;
    vector<int> divisors;
    
    for (int base = 2; base <= 10; base++)
    {
        number = stol(digits, nullptr, base);
        divisor = isPrime(number);
        
        if (divisor != -1) divisors.push_back(divisor);
    }
    
    if (divisors.size() == 9) /* found jamcoin! print it out */
    {
        nJamcoins++;
        
        fout << digits << " ";
        
        for (int i = 0; i < 9; i++)
            fout << divisors[i] << " ";
        fout << endl;
    }
}

void findJamcoins(string digits, int n, int check) /* Should take care of duplicate calculation problem */
{
    if (n == (N - 1)) return;
    if (nJamcoins >= J) return;
    
    if (check != 0) isJamcoin(digits);
    
    findJamcoins(digits, n + 1, 0);
    digits[n + 1] = '1';
    findJamcoins(digits, n + 1, 1);
}

int main(void)
{
    string fileName, digits;
 
    cin >> fileName;
    
    ifstream fin(fileName);
  
    fin >> testCase;
    
    for (int caseN = 0; caseN < testCase; caseN++)
    {
        nJamcoins = 0;
        
        fin >> N >> J;

        for (int i = 0; i < N; i++) digits += '0';
        digits[0] = digits[N - 1] = '1';
        
        fout << "Case #" << caseN + 1 << ":" << endl;
        
        findJamcoins(digits, 0, 1);
        
        digits.clear();
    }
    
    return 0;
}
