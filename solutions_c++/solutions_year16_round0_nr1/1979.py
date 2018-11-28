/* 
 * File:   main.cpp
 * Author: juro
 *
 * Created on April 9, 2016, 11:17 PM
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

/*
 * 
 */

void fillNums(long long num, set<int> &fig) {
    while (num > 0) {
        fig.insert(num % 10);
        num /= 10;
    }
}

int main(int argc, char** argv) {

    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        long long n;
        cin >> n;
        printf("Case #%d: ", i+1);
        if (n == 0) cout << "INSOMNIA" << endl;
        else {
            set<int> fig;
            long long curr = n;
            while (fig.size() != 10) {
                fillNums(curr, fig);
                if (fig.size() == 10) {
                    printf("%lld\n", curr);
                    break;
                }
                curr += n;
            }
        }
    }
    
    return 0;
}

