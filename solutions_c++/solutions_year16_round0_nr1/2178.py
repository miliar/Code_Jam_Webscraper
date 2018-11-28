#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_set>
using namespace std;

const string fail = "INSOMNIA";

void split(int x, unordered_set<int>& st) {
    while (x != 0) {
        st.insert(x % 10);
        x /= 10;
    }
}

int solve(int x) {
    int cur = x;
    unordered_set<int> st;
    split(x, st);
    while (st.size() < 10) {
        cur += x;
        split(cur, st);
    }
    return cur;
}

int main()
{
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++cas);
        int x;
        scanf("%d", &x);
        if (x == 0) {
            printf("%s\n", fail.c_str());
        } else {
            printf("%d\n", solve(x));
        }
    }
    return 0;
}