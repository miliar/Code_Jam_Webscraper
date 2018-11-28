#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <cstdint>

using namespace std;

void coinJam(int N, int J);
void printBinary(int value, int repeat);
void printFactor(int value);


int main(){
    
    int numOfTest = 0;
    int count = 0;
    string line;

    if(getline(cin, line)){
        numOfTest = stoi(line);
    }
    else{
        cout << "No testcase is specified.\n";
        return 1;
    }

    while(getline(cin, line)) {
        string::size_type sz;
        int n = stoi(line, &sz);
        int j = stoi(line.substr(sz));

        cout << "Case #" << ++count << ": " << endl;
        coinJam(n, j);
    }
    return 0;

}

void coinJam(int N, int J){

    int count = 0, divisor = (N/2);
    // cout << "Debug: " << N << ", " << J << endl; 
    unordered_set<int> myset;

    while(divisor >= 2){
        if(N % divisor == 0){
            int repeat = N / divisor;
            int permutation = divisor-2;
            int upper = (1 << permutation) - 1;
            int begin = (1 << (divisor-1)) + 1;
            int temp = begin;
            int idx = 0;

            auto got = myset.find(temp);
            if(got == myset.end()){
                printBinary(temp, repeat);
                printFactor(temp);
                myset.insert(temp);
                count++;
            }

            // cout << "Debug: " << upper << endl;
            while(idx < upper){
                temp += 2;
                
                auto got = myset.find (temp);
                if(got == myset.end()){
                    printBinary(temp, repeat);
                    printFactor(temp);
                    myset.insert(temp);
                    count++;
                }

                idx++;
                if(count >= J)
                    return;
            }
        }
        divisor--;
    }

    if(count < J)
        cout << "Alert!\n";
}

void printBinary(int value, int repeat){
    
    string temp = "";
    do{
        temp += '0' + (value % 2);
        value /= 2;
    }while(value);
    
    reverse(temp.begin(), temp.end());
    for(int i = 0; i < repeat; i++)
        cout << temp;
}

void printFactor(int value){

    for(int base = 2; base < 11; base++){
        
        int temp = value;
        __int128 multiplier = 1;
        __int128 sum = 0;
        
        while(temp != 0){
            int digit = temp & 0x01;
            sum += multiplier * digit;
            multiplier *= base;
            temp >>= 1;
        }
        printf(" %llu", sum);
        // cout << " " << sum;
    }

    cout << endl;
}



