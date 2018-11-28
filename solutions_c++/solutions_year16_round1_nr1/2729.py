//
//  main.cpp
//  codejam
//
//  Created by Todor Lyubomirov Bonchev on 1/1/16.
//

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <stack>
#include <set>
#include <deque>

using namespace std;
void solve() {
    string word;
    cin >> word;
    deque<char> res;
    res.push_back(word[0]);
    for (int i = 1; i < word.size();++i) {
        if (word[i] < res[0]) {
            res.push_back(word[i]);
        } else {
            res.push_front(word[i]);
        }
    }
    string rez;
    for (int i=0;i<res.size();++i) {
        rez.push_back(res[i]);
    }
    cout << " " <<  rez << endl;
}

int main(int argc, const char * argv[]) {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int tests;
    scanf("%d\n", &tests);
    for (int test=1;test<=tests;++test) {
        printf("Case #%d:", test);
        solve();
    }

    return 0;
}
