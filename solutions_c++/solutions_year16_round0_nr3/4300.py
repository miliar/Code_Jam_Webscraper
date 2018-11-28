//
//  main.cpp
//  CoinJam
//
//  Created by Eben on 2016/04/09.
//  Copyright © 2016 Eben. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <pthread.h>

using namespace std;


bool isPrime (int num)
{
    if (num <=1)
        return false;
    else if (num == 2)
        return true;
    else if (num % 2 == 0)
        return false;
    else
    {
        bool prime = true;
        int divisor = 3;
        double num_d = static_cast<double>(num);
        int upperLimit = static_cast<int>(sqrt(num_d) +1);
        
        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
                prime = false;
            divisor +=2;
        }
        return prime;
    }
}


int main() {
    ifstream inFile;
    cout << "Give the file name: ";
    string fileName;
    cin >> fileName;
    
    inFile.open(fileName.c_str());
    if (!inFile){
        cout << "file" << fileName << " not found" << endl;
        return 0;
    }
    ofstream outFile("output.txt");
    outFile << "Case #1:";
    int amountOfCases;
    inFile >> amountOfCases;
//    amountOfCases = 1;
    int amountOfDigits;
    inFile >> amountOfDigits;
//    amountOfDigits = 16;
    int amountOfCoins;
    inFile >> amountOfCoins;
//    amountOfCoins = 50;
    int foundCoins = 0;
    
    int nTemp = (int)pow(2, amountOfDigits) - 1;
    string coin(amountOfDigits,'0');
    string prevCoin(amountOfDigits,'0');
    for (int i = 0; i <= nTemp; i++)
    {
        if(foundCoins == amountOfCoins){
            outFile.close();
            return 0;

        }
        for (int k = 1; k < amountOfDigits-1; k++)
        {
            if ((i >> k) & 0x1)
            {
                
                coin[k] = '1';
            }
            else
            {
                
                coin[k] = '0';
            }
            
        }
        coin[0]='1';
        coin[amountOfDigits-1]='1';
        cout << coin<< endl;
        if (coin != prevCoin){
        if (foundCoins == amountOfCoins)
        {
            outFile.close();
            cout << "finished YAY -------"<< endl;
            return 0;
        }
        bool allBasesNotPrime = true;
        int base = 2;
        while (base <= 10 && allBasesNotPrime) {
            unsigned long long toInt = stoull(coin,0,base);
            bool isDiv = false;
            for (int div = 2; div < toInt/2; ++div) {
                if (toInt % div == 0){
                    isDiv = true;
                    break;
                }
            }
//            bool isDiv = !isPrime(toInt);
            
            
            if (!isDiv){
                allBasesNotPrime = false;
                break;
            }
            base ++;
        }
        if (allBasesNotPrime){
            outFile << endl <<coin << " ";
            cout << endl <<coin << " ";
            foundCoins += 1;
            prevCoin = coin;
            for (int base = 2; base <=10; base++) {
                unsigned long long toInt = stoull(coin,0,base);
                for (int div = 2; div < toInt/2; ++div) {
                    if (toInt % div == 0){
                        cout <<div << " ";
                        outFile <<div << " " ;
                        break;
                    }
                }
            }
        }

        }
    }
    
        outFile.close();
    
    cout << "finished YAY --not----"<< endl;
        return 0;
}


