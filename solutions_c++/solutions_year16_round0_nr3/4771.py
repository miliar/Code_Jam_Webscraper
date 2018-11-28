//
//  main.cpp
//  CoinJam
//
//  Created by YOUQingfei on 4/10/16.
//  Copyright © 2016 YOUQingfei. All rights reserved.
//

#include <iostream>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

int T = 1;
int N, J;
bool isAlwaysNotPrime = true;

map<long long, vector<long long>> mp;

void LoadFromFile();
void Compute();
long long CalculateNumFromBase(long long num, int base);
bool isPrime(long long num);
long long GetOnePrime(long long num);
string BinaryForm(long long num);

int main(int argc, const char * argv[]) {
    LoadFromFile();
    Compute();
    
    return 0;
}


void LoadFromFile()
{
    cin >> T;
    cin >> N >> J;
}

long long CalculateNumFromBase(long long num, int base)
{
    long long result = 0;
    for (int i = 0; i < N; ++i)
    {
        long long digit = ((num & (1<<i)) >> i);
        result += digit * (long long) pow(base, i);
    }
    return result;
}

bool isPrime(long long num)
{
    for (long long i = 2; i <= sqrt(num); ++i)
    {
        if (i * (num/i) == num) return false;
    }
    return true;
}

long long GetOnePrime(long long num)
{
    for (long long i = 2; i <= sqrt(num); ++i)
    {
        if (i * (num/i) == num) return i;
    }
    return 0;
}

string BinaryForm(long long num)
{
    string s = "";
    while (num > 0)
    {
        long long digit = (num & 1);
        num >>= 1;
        char c = digit + '0';
        s += c;
    }
    reverse(s.begin(), s.end());
    return s;
}

void Compute()
{
    cout << "Case #1:" << endl;
    int count = 0;
    for (long long i = 0; i < (1<< (N)); ++i)
    {
        if ((i & 1) == 0 || (i & (1<< (N-1))) == 0) continue;
        
        isAlwaysNotPrime = true;
        
        for (int base = 2; base <= 10; ++base)
        {
            long long value = CalculateNumFromBase(i, base);
            if (isPrime(value))
            {
                isAlwaysNotPrime = false;
                break;
            }
        }
        
        if (isAlwaysNotPrime)
        {
            for (int base = 2; base <= 10; ++base)
            {
                long long value = CalculateNumFromBase(i, base);
                long long prime = GetOnePrime(value);
                mp[i].push_back(prime);
            }
            count++;
            
            if (count == J)
            {
                for (auto m : mp)
                {
                    long long number = m.first;
                    auto primes = m.second;
                    cout << BinaryForm(number) << " ";
                    for (auto prime : primes)
                    {
                        cout << prime << " ";
                    }
                    cout << endl;
                }
                return;
            }
        }
    }
}

