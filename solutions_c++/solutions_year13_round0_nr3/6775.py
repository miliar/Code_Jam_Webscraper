/* 
 * File:   main.cpp
 * Author: abhishek
 *
 * Created on April 13, 2013, 12:04 AM
 */

#include <cstdlib>
#include <iostream>
#include <sstream>
#include <vector>
#include<cstdio>
#include <cmath>
using namespace std;

/*
 * 
 */

bool issquare(int n) {
    if (n < 0)
        return false;

    int root(round(sqrt(n)));

    return (n == root * root);
}

bool ispalin(int j) {
    
    stringstream ss;
    ss << j;
    string str = ss.str();
    if (std::equal(str.begin(), str.begin() + str.size() / 2, str.rbegin()))
        return true;
    else
        return false;
}

int main() {
    int N;
    vector<int>num;
    int count = 0;
    int low, high;
    cin >> N;

    cin.ignore(256, '\n');

    for (int i = 0; i < N; i++) {
        cin >> low >> high;
        // cout<<"  Low   "<<low<<"   high   "<<high<<endl;        
        for (int j = low; j <= high; j++) {
            if (issquare(j)) {
                num.push_back(j);
            }
        }

        for (int k = 0; k < num.size(); k++) {
            if (ispalin(num[k]) && ispalin(sqrt(num[k])))
                count++;
        }
        cout << "Case #" << i + 1 << ": " << count << endl;
        count = 0;
        num.clear();
    }
    return 0;
}

