#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <list>
#include <map>
#include <algorithm>

using namespace std;

string convert(string s) {
    for (int i=0; i<s.length(); i++) {
        s[i] += '0';
    }
    return s;
}

void print_vec(list<int> v) {
    for (auto it=v.begin(); it!=v.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;
}

int reduce_int(int a, int b) {
    int neg = 1;
    if (a < 0) {
        neg *= -1;
        a = -a;
    }
    if (b < 0) {
        neg *= -1;
        b = -b;
    }

    switch (a) {
        case 1:
            return b*neg;
        case 2:
            switch (b) {
                case 1: return a*neg;
                case 2: return -1*neg;
                case 3: return 4*neg;
                case 4: return -3*neg;
            }
        case 3:
            switch (b) {
                case 1: return a*neg;
                case 2: return -4*neg;
                case 3: return -1*neg;
                case 4: return 2*neg;
            }
        case 4:
            switch (b) {
                case 1: return a*neg;
                case 2: return 3*neg;
                case 3: return -2*neg;
                case 4: return -1*neg;
            }
    }
}

// returns rest
list<int> reduce(list<int> i, int obj, bool& failed) {
    if (i.empty()) {
        failed = true;
        return i;
    }

    int a = i.front();
    i.pop_front();
    while (a != obj && !i.empty()) {
        int b = i.front();
        i.pop_front();
        a = reduce_int(a, b);
    }

    if (a != obj) {
        failed = true;
    }

    return i;
}

list<int> reduce_until_empty(list<int> i, int obj, bool& failed) {
    if (i.empty()) {
        failed = true;
        return i;
    }

    int a = i.front();
    i.pop_front();
    while (!i.empty()) {
        int b = i.front();
        i.pop_front();
        a = reduce_int(a, b);
    }

    if (a != obj) {
        failed = true;
    }

    return i;
}
string solve(list<int>& i) {
    //print_vec(i);
    bool failed = false;
    list<int> rest = reduce(i, 2, failed);
    if (failed) return "NO";
    //cout << "found 2, rest: ";
    //print_vec(rest);
    rest = reduce(rest, 3, failed);
    if (failed) return "NO";
    //cout << "found 3, rest: ";
    //print_vec(rest);
    rest = reduce_until_empty(rest, 4, failed);
    if (rest.empty() && !failed) {
        return "YES";
    } else {
        return "NO";
    }
}


int main() {
    int t;
    cin >> t;

    for(int i=1; i <= t; i++) {
        int repeat;
        cin >> repeat;
        cin >> repeat;
        string input;
        cin >> input;
        list<int> input_vec, repeated;

        for (int j=0; j<input.length(); j++) {
            switch (input[j]) {
                case 'i': input_vec.push_back(2); break;
                case 'j': input_vec.push_back(3); break;
                case 'k': input_vec.push_back(4); break;
            }
        }

        for (int j=0; j<repeat; j++) {
            repeated.insert(repeated.end(), input_vec.begin(), input_vec.end());
        }

        cout << "Case #" << i << ": " << solve(repeated) << endl;
    }

    return 0;
}
