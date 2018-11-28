#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> jamcoinBases = { 2, 3, 4, 5, 6, 7, 8, 9, 10 };

string smallest_coin(int N) {
    return "1" + string(N-2, '0') + "1";
}

bool increment_coin(string &coin) {
    for(int i = coin.size() - 2; i >= 1; --i) {
        if(coin[i] == '0') {
            coin[i] = '1';
            return true;
        } else {
            coin[i] = '0';
        }
    }

    return false;
}

vector<uint64_t> primesToTest = { 
      2,     3,     5,     7,    11,    13,    17,    19,    23,    29,
     31,    37,    41,    43,    47,    53,    59,    61,    67,    71,
     73,    79,    83,    89,    97,   101,   103,   107,   109,   113,
    127,   131,   137,   139,   149,   151,   157,   163,   167,   173,
    179,   181,   191,   193,   197,   199,   211,   223,   227,   229
};

uint64_t coin_divisor(const string &coin, int base) {
    long long coinInBase = stoll(coin, nullptr, base);
    for(uint64_t d : primesToTest) {
        if(coinInBase % d == 0) {
            return d;
        }
    }

    return 1;
}

bool all_bases_non_trivial(const string &coin, vector<uint64_t> &divs) {
    for(size_t i = 0; i < jamcoinBases.size(); i++) {
        divs[i] = coin_divisor(coin, jamcoinBases[i]);
        if(divs[i] == 1) {
            return false;
        }
    }

    return true;
}

void printJamcoins(int N, int J) {
    string coin = smallest_coin(N);

    vector<uint64_t> divs(jamcoinBases.size());

    int found = 0;
    do {
        if(all_bases_non_trivial(coin, divs)) {
            cout << coin;
            for(auto div : divs) {
                cout << " " << div;
            }
            //cout << endl << string(N+1, ' ');
            //for(int base : jamcoinBases) {
            //    cout << " " << stoll(coin, nullptr, base);
            //}
            cout << endl;

            found++;
        }
    } while(increment_coin(coin) && found < J);

    if(found < J) {
        throw "not enough coins found";
    }
}

int main() {
    int numCases;
    cin >> numCases;
    
    for(int caseNum = 1; caseNum <= numCases; ++caseNum) {
        cout << "Case #" << caseNum << ": ";

        cout << endl;
        int N, J;
        cin >> N >> J;
        try {
            printJamcoins(N, J);
        } catch(const char *e) {
            cerr << "[error] " << e << endl;
            return 1;
        }

        //cout << endl;
    }
}
