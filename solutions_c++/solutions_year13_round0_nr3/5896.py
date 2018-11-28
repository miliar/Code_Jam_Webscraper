#include <fstream>
#include <iostream>
#include <string.h>
#include <gmp.h>
#include <cmath>

using namespace std;



bool ispalindrom(const string& number) {
    if(number.size() == 1)
        return true;

    size_t i = 0, j = number.size()-1;
    for(; i < j; i++, j--) {
        if( number[i] != number[j] )
            return false;
    }

    return true;
}

bool isSquare(const string& number) {
    mpz_t n1;
    mpz_init(n1);
    mpz_set_str(n1, number.c_str(), 10);

    mpz_t s;
    mpz_init(s);
    mpz_sqrt(s, n1);
    mpz_t n2;
    mpz_init(n2);
    mpz_mul(n2, s, s);

    char ss[102];
    mpz_get_str(ss, 10, s);
    int ret = mpz_cmp(n1, n2);
    mpz_clear(n1); mpz_clear(n2); mpz_clear(s);

    string tmp(ss);
    if( ret == 0 && ispalindrom(tmp))
        return true;
    else
        return false;
}


string nextPalindrom(const string& current) {
    string next;
    int i, j;
    if( current.size() % 2 == 0) {
        i = current.size() / 2-1;
        j = current.size() / 2;
    }
    else {
       i = j = current.size()/2;
    }

    next = current;
    for(; i >= 0 && j < next.size(); i--, j++) {
        if( next[i] != next[j] ) {
            next[j] = next[i];
        }
    }

    mpz_t n1, n2;
    mpz_init(n1); mpz_init(n2);
    mpz_set_str(n1, current.c_str(), 10);
    mpz_set_str(n2, next.c_str(), 10);

    while ( mpz_cmp(n2, n1) <= 0 ) {
        if( current.size() % 2 == 0) {
            i = current.size() / 2-1;
            j = current.size() / 2;
        }
        else
            i = j = current.size()/2;

        for(; i >= 0 && next[i] == '9'; i--, j++);

        if( i >= 0 ) {
            next[i]++;
            if( j != i )
                next[j]++;
            for(i++, j--; i <= j; next[i]=next[j]='0', i++, j--);
        }
        else {
            next.resize(next.size()+1);
            next[0] = '1';
            next[next.size()-1] = '1';
            for(int i = 1; i < next.size()-1; next[i] = '0', i++);
        }

        mpz_set_str(n2, next.c_str(), 10);

    }

    return next;
}



string convertToString(int number) {
    string result;
    while(number) {
        char c = number%10 + '0';
        result.insert(0, 1, c);
        number = number / 10;
    }
    return result;
}

void findFairAndSquare(const string& A, const string& B, int testNum) {
    int total = 0;

    string current = A;
    if( ispalindrom(current) ) {
        if( isSquare(current) )
            total++;
    }
    string next = nextPalindrom(current);
    mpz_t nA;
    mpz_init(nA);
    mpz_set_str(nA, next.c_str(), 10);
    mpz_t nB;
    mpz_init(nB);
    mpz_set_str(nB, B.c_str(), 10);
    while( mpz_cmp(nA, nB) <= 0  ) {
        if( ispalindrom(next) ) {
            if( isSquare(next) )
                total++;
        }

        current = next;
        next = nextPalindrom(current);
        mpz_set_str(nA, next.c_str(), 10);
    }
    mpz_clear(nA); mpz_clear(nB);

/*
    int na = atoi(A.c_str());
    int nb = atoi(B.c_str());
    for(int i = na; i <= nb; i++) {
        int s = int(sqrt(i));
        if( s*s == i) {
            string ss = convertToString(i);
            if(ispalindrom(ss)) {
                total++;
            }
        }
    }
*/

    cout << "Case #" << testNum << ": " << total << endl;

}

int main()
{

    ifstream input("C-small-attempt3.in");
    cin.rdbuf(input.rdbuf());

    ofstream output("C-small-attempt3.out");
    cout.rdbuf(output.rdbuf());


    int T;
    cin >> T;

    string line;
    for(int i = 0; i < T; ) {
        getline(cin, line);
        if( line.empty() )
            continue;
        int ws_index = line.find_first_of(' ');
        string A(line.begin(), line.begin()+ws_index);
        string B(line.begin()+ws_index+1, line.end());

        findFairAndSquare(A, B, i+1);
        i++;

    }

    return 0;
}
