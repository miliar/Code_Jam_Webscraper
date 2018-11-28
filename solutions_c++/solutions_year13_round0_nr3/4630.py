/* 
 * File:   main.cpp
 * Author: SCORPIUS
 *
 * Created on April 13, 2013, 2:27 PM
 */

#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <set>
typedef long long int lli;
using namespace std;
const lli base = (lli) 32;
set<lli> fsq;

template <class T>
inline string to_string(const T t) {
    stringstream ss;
    ss << t;
    return ss.str();
}

bool ispal(string s) {
    bool b = true;
    int l = s.length(), ll = l / 2, i = 0;
    while (b && i < ll) {
        b = !(s[i]^s[l - i - 1]);
        i++;
    }
    return b;
}

string nxtpal(string s) {
    int l = s.length(), ll = l / 2;
    if (s[ll] != '9') {
        s[ll]++;
        s[ll - 1] += !(l & 1);
    } else {
        int k = ll;
        s[ll] = '0';
        if (!(l & 1)) {
            s[--k] = '0';
        }
        while (k > 0 && s[--k] == '9') {
            s[k] = '0';
            if (s[++ll] == '9')s[ll] = '0';
        }
        if (k > 0) {
            s[k]++;
            s[++ll]++;
        } else if (k == 0 && s[k] != '0') {
            s[k]++;
            s[++ll]++;
        } else if (k == 0 && s[k] == '0') {
            s[k] = '1';
            s += '1';
        }
    }
    return s;
}
lli sll(string s){
    int l=s.length();lli k=0;
    for(int i=0;i<l;i++){
        k*=10;
        k+=(s[i]-'0');
    }
    return k;
}

int main() {
    lli t, i = 0;
    cin >> t;
    while (i < base) {
        lli z = i*i;
        if (ispal(to_string(z))) fsq.insert(z);
        i = sll(nxtpal(to_string(i)));
    }
    for (int i = 1; i <= t; i++) {
        int y, a, b;
        cin >> a >> b;
        if (a > b) {
            a += b;
            b = a - b;
            a = a - b;
        }
        printf("Case #%d: ", i);
        cout << distance(fsq.lower_bound(a), fsq.upper_bound(b)) << endl;
    }

    // cout<<ispal("STRTS")<<ispal("GSDDSG")<<endl;
    // cout<<nxtpal("13431")<<" "<<nxtpal("999999")<<" "<<nxtpal("139931")<<" "<<nxtpal("5489845");
    return 0;
}
