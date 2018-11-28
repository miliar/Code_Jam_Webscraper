//
//  REVERSE.cpp
//  
//
//  Created by Manh Le on 9/4/16.
//
//

#include <iostream>
#include <cstdio>
#include <string>
#include <vector> 

using namespace std;

void openFile() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
}

void solve(string st) {
    
    int n = st.size() - 1;
    int result = 0;
    while (n >= 0) {
        result++;
        int i = n;
        while (i >= 0 && st[i] == st[n]) {
            i--;
        }
        n = i;
    }
    
    if (st[st.size() - 1] == '+') {
        result--;
    }
    cout << result << endl;
}

void process() {
    
    int test;
    scanf("%d\n", &test);
    for(int t = 1; t <= test; t++) {
        string st;
        getline(cin, st);
        cout << "Case #" << t << ": ";
        solve(st);
    }
    
}

int main() {
    
    openFile();
    process();
    
    return 0;
}
