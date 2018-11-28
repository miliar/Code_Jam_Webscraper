//
//  main.cpp
//  GoogleJam
//
//  Created by Isira Samarasekera on 3/13/16.
//  Copyright (c) 2016 Isira Samarasekera. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <numeric>
#include <math.h>
using namespace std;

#define SIZE 16

long bitvalue(string bits, int base)
{
    long total = 0;
    for(int i=0; i < bits.size(); i++)
    {
        char c = bits[i];
        int val = 0;
        if(c=='1')
            val = 1;
        
        total = total*base + val;
    }
    return total;
}
bool isPrime(long num)
{
    if(num == 2)
        return true;
    if(num %2 == 0)
        return false;
    long till = ceil(sqrt(num))+1;
    for(int i= 2; i < till; i++)
    {
        if((num % i) == 0)
            return false;
    }
    return true;
}

string get_bitSetvalue(std::bitset<SIZE> mybits, int base)
{
    long val= 0;
    for(int k=mybits.size()-1; k >= 0; k--)
    {
        val = val*base + mybits[k];
    }
    return to_string(val);
}

bool isDividingAllBases(string bitString)
{
    for(int i=2; i <=10; i++)
    {
        if(isPrime(bitvalue(bitString, i)))
            return false;
    }
    return true;
}

long findAFactor(string bitString, int base)
{
    long val = bitvalue(bitString, base);
    int i = 3;
    while(val%i != 0)
    {
        i+=2;
    }
    return i;
}

vector<vector<string>>  findBits(int N, int J)
{
    int min = pow(2, N-1)+1;
    int max = pow(2, N);
    map<int, int> vals;
    vector<vector<string>> values;
    for(int i= max - 1, k =0; k < 10 && (i >= min); i-=2)
    {
        std::bitset<SIZE> mybits(i);
        std::string mystring =
        mybits.to_string<char,std::string::traits_type,std::string::allocator_type>();
        if(isDividingAllBases(mystring))
        {
            vector<string> val;
            val.push_back(mystring);
            for(int j = 2; j <= 10; j++)
            {
                val.push_back(to_string(findAFactor(mystring, j)));
            }
            k++;
            
            values.push_back(val);
        }
    }
    return values;
}

void test()
{
        ifstream in("/Users/isira/Documents/C-small-out-2.out");
        string line;
    for(int i= 0; i < 50; i++)
    {
        getline(in, line);
        stringstream ss(line);
        
        string bitString;
        getline(ss,bitString, ' ');
        cout<< bitString << " "<< isDividingAllBases(bitString);
        for(int k=2; k <=10; k++)
        {
            string num;
            getline(ss,num, ' ');
            long n = stol(num);
            cout<<" "<<k<<": "<<(bitvalue(bitString, k)%n);
        }
        cout<<endl;
    }
}

int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream in("/Users/isira/Documents/C-small-attempt0.in");
    ofstream out("/Users/isira/Documents/C-small.out");
    string line;
    getline(in, line);
    
    int nTests =0;
    nTests = stoi(line);
    for(int i= 0; i < nTests; i++)
    {
        getline(in, line);
        stringstream ss(line);
        
        string token;
        getline(ss,token, ' ');
        
        int N = stoi(token);
        getline(ss,token, ' ');
        int J = stoi(token);
        out<<"Case #"<<i+1 <<": "<<endl;
        vector<vector<string>> values = findBits(N, J);
        
        for(auto it= values.begin(); it != values.end(); it++)
        {
            vector<string> val = *it;
            for(auto it1= val.begin(); it1 != val.end(); it1++)
            {
                out<<*it1<<" ";
            }
            out<<endl;
        }

    }

    in.close();
    out.close();

    return 0;
}
