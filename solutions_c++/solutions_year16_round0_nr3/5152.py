#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

void getFromFile (ifstream &ifl, vector<int> &len, vector<int> &num){
    int n;
    ifl >> n;
    int k = 0;
    for (int i = 0; i < n; ++i){
        ifl >> k;
        len.push_back (k);
        ifl >> k;
        num.push_back (k);
    }
}

vector<bool> getVectorFromString (string str){
    vector<bool> result;
    for (int i = 0; i < str.length(); ++i){
        if (str[i] == '1')
            result.push_back(true);
        else
            result.push_back(false);
    }
    return result;
}

bool isPrimeNumber (long unsigned int num){
    if (num == 1 || num == 2 || num == 3)
        return true;
    if (num%2 == 0)
        return false;
    for (int i = 3; (i*i) <= num; i+= 2){
        if (num%i == 0)
            return false;
    }
    return true;
}

long unsigned int getBinaryEquivalent (const char *str, int length,unsigned int base){
    long unsigned int result = 0;
    for (int i = 0; i < length; ++i){
        if (str[i] == '1')
            result += static_cast<long unsigned int> (powl (base, length-i-1));
    }
    return result;
}

string getBinaryOfNumber(unsigned long int num, int length){
    char *res = new char[length+1];
    res[length] = '\0';
    for (int i = 0; i < length; ++i)
        res[i] = '0';
    int pos;
    int index = length-1;
    while (num > 0){
        if (num%2 == 0)
            res[index] = '0';
        else
            res[index] = '1';
        num /= 2;
        index--;
    }
    /*
    while (getBinaryEquivalent(res, length, 2) != num){
        pos = rand() % length;
        if (res[pos] == '1')
            res[pos] = '0';
        else
            res[pos] = '1';
    }
    */
    return string(res);
}

vector<string> getAllJamCoins (int length){
    length -= 2;
    vector<string> result;
    long unsigned int i = 0, upto;
    upto = static_cast<long unsigned int> (powl(2,length));
    string str = "";
    for (; i < upto; ++i){
        str = getBinaryOfNumber(i, length);
        str = string("1") + str + string("1");

        if(!isPrimeNumber(getBinaryEquivalent(str.c_str(),length+2,2)) &&
            !isPrimeNumber(getBinaryEquivalent(str.c_str(),length+2,3)) &&
            !isPrimeNumber(getBinaryEquivalent(str.c_str(),length+2,4)) &&
            !isPrimeNumber(getBinaryEquivalent(str.c_str(),length+2,5)) &&
            !isPrimeNumber(getBinaryEquivalent(str.c_str(),length+2,6)) &&
            !isPrimeNumber(getBinaryEquivalent(str.c_str(),length+2,7)) &&
            !isPrimeNumber(getBinaryEquivalent(str.c_str(),length+2,8)) &&
            !isPrimeNumber(getBinaryEquivalent(str.c_str(),length+2,9)) &&
            !isPrimeNumber(getBinaryEquivalent(str.c_str(),length+2,10))
        ){
            cout << i << " : " << str << endl;
            result.push_back(str);
        }
    }
    cout << "end of getAllJamCoins" << endl;
    return result;
}
long unsigned int getNonTrivialDivisor (long unsigned int num){
    //return num;
    for (long unsigned int i = sqrt(num); i >= 2; --i){
        if (num%i == 0){
            return i;
        }
    }
    return -200;
}

void process(ofstream &outf, vector<int> lengths, vector<int> numbers){
    vector<string> jamCoins;
    int length, num;
    for (int i = 0; i < lengths.size(); ++i){
        length = lengths[i];
        num = numbers[i];
        jamCoins = getAllJamCoins(length);
        cout << "end of process";
        outf << "Case #" << i+1 << ":\n";
        for (int j = 0; j < num; ++j){
            cout << "inside loop" << endl;
            outf << jamCoins[j]
                 << " " << getNonTrivialDivisor(getBinaryEquivalent(jamCoins[j].c_str(),length,2))
                 << " " << getNonTrivialDivisor(getBinaryEquivalent(jamCoins[j].c_str(),length,3))
                 << " " << getNonTrivialDivisor(getBinaryEquivalent(jamCoins[j].c_str(),length,4))
                 << " " << getNonTrivialDivisor(getBinaryEquivalent(jamCoins[j].c_str(),length,5))
                 << " " << getNonTrivialDivisor(getBinaryEquivalent(jamCoins[j].c_str(),length,6))
                 << " " << getNonTrivialDivisor(getBinaryEquivalent(jamCoins[j].c_str(),length,7))
                 << " " << getNonTrivialDivisor(getBinaryEquivalent(jamCoins[j].c_str(),length,8))
                 << " " << getNonTrivialDivisor(getBinaryEquivalent(jamCoins[j].c_str(),length,9))
                 << " " << getNonTrivialDivisor(getBinaryEquivalent(jamCoins[j].c_str(),length,10))
                 << "\n";
        }
    }
}
int main (void){
    srand (time(NULL));
    cout << "started..." << endl;
    ifstream infile ("C-small-attempt1.in");
    ofstream outfile ("C-small.out");
    std::vector<int> lengths, numbers;
    getFromFile (infile, lengths, numbers);
    process (outfile, lengths, numbers);
    return 0;
}
