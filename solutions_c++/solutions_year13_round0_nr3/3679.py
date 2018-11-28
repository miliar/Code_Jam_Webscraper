#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "BigIntegerLibrary.hh"
using namespace std;

bool isPalindrome(const string& text) {
    for (int i = 0; i < text.size() / 2; i++) {
        if (text[i] != text[text.size()-1-i])
            return false;
    }

    return true;
}

template<typename Iter>
bool next(Iter begin, Iter end) {
    while (begin != end) {
        --end;
        if ((*end & 1) == 0) {
            ++(*end);
            return true;
        }
        else
            --(*end);
    }

    return false;
}

string rev(const string& str) {
    return string(str.rbegin(), str.rend());
}

bool onesOk(const string& str) {
    int result = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '1')
            result++;
        if (result > 3)
            return false;
    }
    return true;
}

vector<string> all(string str) {
    vector<string> comb;

    do {
        if (onesOk(str))
            comb.push_back(str);
    } while (next(str.begin(), str.end()));

    return comb;
}

void check(const string& str, ofstream& file) {
    BigInteger b = stringToBigInteger(str);
    string bd = bigIntegerToString(b*b);

    if (isPalindrome(bd))
        file << bd << endl;
}

void generateAllPossible(int start, int end) {
    string str = "0";

    for (int i = 0; i < start - 1; i++)
        str += "0";

    ostringstream ss;
    ss << "test_" << start << "" << end << ".txt";

    ofstream file(ss.str());
    int length = start;

    while (length <= end) {
        vector<string> allPos = all(str);
        
        for (int i = 0; i < allPos.size(); i++) {
            check("1" + allPos[i] + rev(allPos[i]) + "1", file);
        }

        check("2" + str + str + "2", file);
        
        for (int i = 0; i < allPos.size(); i++) {
            check("1" + allPos[i] + "0" + rev(allPos[i]) + "1", file);
            check("1" + allPos[i] + "1" + rev(allPos[i]) + "1", file);
            check("1" + allPos[i] + "2" + rev(allPos[i]) + "1", file);
        }

        check("2" + str + "0" + str + "2", file);
        check("2" + str + "1" + str + "2", file);

        length++;
        str += "0";
        cout << length << endl;
    }

    file.close();
}

int findPos(const vector<BigInteger>& v, const BigInteger& b) {
    for (int i = 0; i < v.size(); i++) {
        if (v[i] > b)
            return i;
    }

    return -1;
}

int main(char* argv[]) {
    ios_base::sync_with_stdio(false);
    
    vector<BigInteger> v(50000);
    ifstream file("data.txt");

    string line;
    while (!file.eof()) {
        file >> line;
        v.push_back(stringToBigInteger(line));
    }

    file.close();

    int T;
    string Ns, Ms;

    cin >> T;

    for (int i = 0; i < T; i++) {
        cin >> Ns >> Ms;

        BigInteger N = stringToBigInteger(Ns) - 1;
        BigInteger M = stringToBigInteger(Ms);

        int np = findPos(v, N);
        int mp = findPos(v, M);

        cout << "Case #" << i+1 << ": " << mp-np << endl;
    }

    /*int N, M;
    cin >> N >> M;
    generateAllPossible(N, M);
    cout << "OK " << N << " " << M << endl;*/

    return 0;
}