/*
 * vim: set ts=4, sts=4, sw=4
 * Copyright (c) 2015 Lynn Tran
 */

#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cmath>
#include<map>
#include <sstream>
#include<set>
using namespace std;

void initSet(set<int>& s) {
    s.insert(0);
    s.insert(1);
    s.insert(2);
    s.insert(3);
    s.insert(4);
    s.insert(5);
    s.insert(6);
    s.insert(7);
    s.insert(8);
    s.insert(9);
}

void getDigits(int number, set<int>& s) {
    do {
        int digit = number % 10;
        s.insert(digit);
        number /= 10;
    }
    while (number > 0);
}

bool check(set<int> origin, const set<int> ret) {
    set<int>::iterator it;
    int count = 0;
    for (set<int>::iterator it1 = origin.begin(); it1 != origin.end(); it1++) {
        it = ret.find(*it1);
        if (it != ret.end()) {
            count++;
        }
    }

    if (count == origin.size()) {
        return true;
    }
    return false;
}

int main(){
    int t;
    cin >> t;
    set<int> s;
    initSet(s);

    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i+1);
        int a[10];
        int n, j = 1;

        cin >> n;
        if (n == 0) {
            cout << "INSOMNIA\n";
            continue;
        }
        set<int> ret;
        bool found = false;

        while (j <= 1000000) {
            int temp = n * j;

            getDigits(temp, ret);
            if (check(s, ret)) {
                cout << temp;
                found = true;
                break;
            }

            j++;
        }

        if (!found) {
            cout << "INSOMNIA";
        }

        cout << endl;
    }
}
