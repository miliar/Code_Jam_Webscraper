//
//  main.cpp
//  codejam
//
//  Created by Saurabh Goyal on 09/04/16.
//  Copyright © 2016 saurabhgoyal. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;
/*
class BigNum{
    unsigned long long a=0;
    unsigned long long b=0;
    
    bool isPrime();
};

bool BigNum::isPrime(){
    bool flag = true;
    while (flag) {
        
    }
    return false;
}
*/
vector<unsigned long long> primes;

unsigned long long isPrime(unsigned long long &num)
{
    for (int i=0; i<primes.size(); i++) {
        if (primes[i]*primes[i] > num) break;
        if (primes[i]*primes[i] < primes[i]) break;
        if(num%primes[i] == 0)
            return primes[i];
    }
    return 1;
}

void generatePrime()
{
    if(primes.size() == 0){
        primes.push_back(2);
        primes.push_back(3);
        primes.push_back(5);
        primes.push_back(7);
        primes.push_back(11);
        primes.push_back(13);
        primes.push_back(17);
        primes.push_back(19);
        primes.push_back(23);
        primes.push_back(29);
        primes.push_back(31);
    }
    
    for (unsigned long long i=primes[primes.size()-1]+2; i<100000000; i+=2) {
        if (isPrime(i) == 1) {
            primes.push_back(i);
        }
    }
}

unsigned long long base(unsigned long long num, int n){
    unsigned long long temp = num;
    unsigned long long newNum = 0;
    for (int i=0; temp != 0; i++) {
        newNum += (temp%10)*pow(double(n), double(i));
        temp = temp/10;
    }
    return newNum;
}

unsigned long long isCoinJamForBase(unsigned long long num, int n){
    num = base(num, n);
    return isPrime(num);
}

unsigned long long nextNum(unsigned long long num){
    bool flag = true;
    for(int i=1; flag; i++) {
        unsigned long long num1 = num / (unsigned long long)(pow(double(10), double(i)));
        unsigned long long temp1 = num % (unsigned long long)(pow(double(10), double(i)));
        unsigned long long temp = temp1 / (unsigned long long)(pow(double(10), double(i-1)));
        if (temp == 0) {
            num = num1 * (unsigned long long)(pow(double(10), double(i)));
            num += (unsigned long long)(pow(double(10), double(i-1)));
            num += 1;
            flag = false;
        }
    }
    return num;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    
    generatePrime();
//    bool digits[16] = {false};
    
    cout << "prime ready" << endl;
    ofstream ofile;
    ofile.open ("output.txt");
    ofile << "Case #" << 1 <<": " << endl;

    unsigned long long factors[9] = {0};
    int count = 0;
    for (unsigned long long i=1000000000000001; count<50; i = nextNum(i)) {
        factors[0] = isCoinJamForBase(i, 2);
        if (factors[0] == 1)
            continue;
        factors[1] = isCoinJamForBase(i, 3);
        if (factors[1] == 1)
            continue;
        factors[2] = isCoinJamForBase(i, 4);
        if (factors[2] == 1)
            continue;
        factors[3] = isCoinJamForBase(i, 5);
        if (factors[3] == 1)
            continue;
        factors[4] = isCoinJamForBase(i, 6);
        if (factors[4] == 1)
            continue;
        factors[5] = isCoinJamForBase(i, 7);
        if (factors[5] == 1)
            continue;
        factors[6] = isCoinJamForBase(i, 8);
        if (factors[6] == 1)
            continue;
        factors[7] = isCoinJamForBase(i, 9);
        if (factors[7] == 1)
            continue;
        factors[8] = isPrime(i);
        if (factors[8] == 1)
            continue;
        
        count++;
        cout << i;
        ofile << i;
        for (int j=0; j<9; j++) {
            cout << " " << factors[j];
            ofile << " " << factors[j];
        }
        cout << endl;
        ofile << endl;
/*
        if (isCoinJamForBase(i, 2) && isCoinJamForBase(i, 3) && isCoinJamForBase(i, 4) && isCoinJamForBase(i, 5) && isCoinJamForBase(i, 6) && isCoinJamForBase(i, 7) && isCoinJamForBase(i, 8) && isCoinJamForBase(i, 9) && !isPrime(i)) {
            cout << i << endl;
            count++;
        }
 */
//        cout << i << endl;
    }
    ofile.close();
    return 0;
}

/*
int countJump(string& str){
    int count = 0;
    unsigned long length = str.length();

    for (int i=1; i<length; i++) {
        if (str[i] != str[i-1])
            count++;
    }
    return count;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    string line;
    ifstream ifile ("B-large.in.txt");
    ofstream ofile;
    ofile.open ("output.txt");

    if (ifile.is_open() && ofile.is_open())
    {
        getline (ifile,line);
        int totalCases = stoi(line);
        
        for(int i=1; getline (ifile,line) && i<=totalCases; i++)
        {
            int count = countJump(line);
            if(line[line.length()-1] == '-')
                count++;
            
            ofile << "Case #" << i <<": " << count << endl;
            
        }
        ifile.close();
        ofile.close();
    }
    
    else cout << "Unable to open file";
    
    return 0;
}
 */
