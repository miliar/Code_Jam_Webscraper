#include <iostream>
#include <fstream>

#include <vector>
#include <math.h>

using namespace std;

unsigned long long isPrime(unsigned long long);
unsigned long long binaryToBase(string, int);
bool isJamcoin(string, int, int*);
int getFirstDivisor(unsigned long);

int main(){
    ofstream outputFile ("output.txt");
    ifstream inputFile ("C-small-attempt1.in");
    int cases;

    inputFile >> cases;

    for(int c = 0; c < cases; c++){
        int jamLength, jamCount, jamIndex, _pc, jamCounter = 0;
        bool done = false;

        inputFile >> jamLength;
        inputFile >> jamCount;

        vector<string> jamcoins;
        jamIndex = 0;

        // Come on and Slam, and welcome to the Jam(Coin generator)
        cout << "Case #" << (c + 1) << ":\n";
        outputFile << "Case #" << (c + 1) << ":\n";

        // Find Possible JAMCOINS
        while(!done){
            jamCounter += 1;
            //cout << "jamCounter: " << jamCounter << "\n";
            // generate binary JAMCOIN
            string _jamcoin;

            _jamcoin = bitset<64>(jamCounter).to_string();

            //cout << "raw _jamcoin: " << _jamcoin << "\n";

            // clean JAMCOIN
            for(int sub = 0; sub < _jamcoin.length(); sub++){
                if(_jamcoin[sub] == '1'){
                    if(sub > 0){
                        _jamcoin = _jamcoin.substr(sub);

                        //cout << "substr: " << _jamcoin << "\n";
                    }

                    break;
                }
            }

            _jamcoin = "1" + _jamcoin + "1";

            // determine if this is a good jamcoin
            int divisors[9];

            //cout << "jamcoin: " << _jamcoin << "\n";

            if(_jamcoin.length() == jamLength && isJamcoin(_jamcoin, jamLength, divisors)){

                jamcoins.push_back(_jamcoin);
                jamIndex += 1;

                cout << "jamcoin: " << _jamcoin << " ";
                outputFile << _jamcoin << " ";

                // Compute Divisors
                for(int d = 2; d <= 10; d++){
                    //unsigned long val = binaryToBase(_jamcoin, d);
                    //int divisor = getFirstDivisor(val);
                    int divisor = divisors[(d - 2)];

                    cout << divisor << " ";
                    outputFile << divisor << " ";

                    //divisors[d - 2] = divisor;
                }

                cout << "\n";
                outputFile << "\n";

                if(jamIndex >= jamCount){
                    done = true;
                    break;
                }
            }
        }
    }


    outputFile.close();
    inputFile.close();

    return 0;
}

int getFirstDivisor(unsigned long value){
    //cout << "\tGetting divisor of " << value << "\n";

    for(unsigned long long i = 2; i < value; i += 1){
        if(value % i == 0)
            return i;
    }

    return -1;
}

bool isJamcoin(string jamcoin, int len, int * divisors){
    bool hasWrapper = jamcoin[0] == '1' &&
                      jamcoin[jamcoin.length() - 1] == '1';
    bool isCorrectLength = jamcoin.length() == len;
    bool basesCorrect = false;

    int basesCorrectCount = 0;
    for(int base = 2; base <= 10; base++){
        unsigned long long val = binaryToBase(jamcoin, base);
        int divisor = isPrime(val);

        //cout << "\t\t\tval:" << val << "\n";

        if(divisor != -1){
            basesCorrectCount += 1;
        }

        //cout << "\t\tdivisor: " << divisor << "\n";

        divisors[(base - 2)] = divisor;
    }

    if(basesCorrectCount >= 9){
        //cout << "\thotdog.\n";

        basesCorrect = true;
    }

    //cout << "basesCorrectCount: " << basesCorrectCount << "\n";

    //cout << "hasWrapper: " << hasWrapper << "\n";
    //cout << "isCorrectLength: " << isCorrectLength << "\n";
    //cout << "\tjamcoin.length(): " << jamcoin.length() << "\n";
    //cout << "\tlen:" << len << "\n";

    return hasWrapper && isCorrectLength && basesCorrect;
}

unsigned long long isPrime(unsigned long long n){
    //cout << "\tn: " << n << "\n";

    if(n%1 || n < 2){
        return -1;
    }
    if(n%2 == 0){
        return 2;
    }
    if(n%3 == 0){
        return  3;
    }

    int m = (int)sqrt(n);

    for(int i = 5; i <= m; i += 6){
        if (n%i == 0){
            return i;
        }
        if (n%(i + 2) == 0){
            return (i + 2);
        }
    }

    return -1;
}

unsigned long long binaryToBase(string binary, int base){
    unsigned long long total = 0;

    for(int s = 0; s < binary.length(); s++){
        int pos = (binary.length() - 1) - s;
        char currChar = binary[pos];

        if(currChar == '1'){
            total += pow(base, s);
        }
    }

    return total;
}
