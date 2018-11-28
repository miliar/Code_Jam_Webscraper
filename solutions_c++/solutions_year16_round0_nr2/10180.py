#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <string>
#include <list>
#include <queue>
#include <functional>
#include <stack>
#define INF 210566789
using namespace std;
int test;
int main() {
    int i = 1;
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    cin >> test;
    while (i <= test) {
        int shift = 0;
        string str;
        char ch;
        cin >> str;
        ch = str[0];
        int j=1;
        for (j = 1; j < str.length(); j++) {
            if (ch != str[j]) {
                shift++;
                ch = str[j];
            }
        }
        if (str[j - 1] == '-') shift++;
        cout << "Case #" << i << ": " << shift<<endl;
        i++;
    }
    return 0;
}