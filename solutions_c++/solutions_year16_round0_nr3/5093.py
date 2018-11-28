/*
 * coin_jam.cpp
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <bitset>

using namespace std;


long long strToDec(string, int);

int main(int argc, char **argv) {

    /* gotta deal with the constness of the input variables, no time, will figure out later */
    /* input for this problem is deterministic so it doesnt matter */


    const int N = 32;
    const int J = 500;
    const int strLen = N/2 - 2;
    
    string factor = bitset<N/2+1>(pow(2,N/2)+1).to_string();
    /*
    string factor = "1";
    int k;
    for (k = 0; k < N/2 - 1; k++) {
        factor += "0";
    }
    factor += "1";
    */
    //cout << factor << endl;

    cout << "Case #1:" << endl;


    int i;
    string subStr;
    for (i = 0; i < J && i < pow(2, strLen); i++) {

        subStr = bitset<strLen>(i).to_string();
        subStr = "1" + subStr + "11" + subStr + "1";
        cout << subStr << " " ;

        /* only do up to base 9, the strToDec function doesn't like such big input for some reason, probably some integer overflow from pow function */
        int j;
        for (j = 2; j <= 9; j++) {
            cout << strToDec(factor, j) << " " ;
        }

        /* do base 10 */

        cout << factor << endl;

        /* this is converts the number to decimal, so we can check our answer */
        /*
        for (j = 2; j <= 9; j++) {
            cout << strToDec(subStr, j) << " " ;
        }
        cout << endl;
        */
    }

    return 0;
}

long long strToDec(string s, int base) {
    int N = s.length();
    int i;
    long long output = 0;
    for (i = 0; i < N; i++) {
        //cout << s[N-i-1] << endl;
        if (s[N - 1 - i] == '1') {
            output += pow(base, i);
        }
    }
    return output;
}
