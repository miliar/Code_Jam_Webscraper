/*
 * Author: fatboy_cw
 * Created Time:  2016年04月09日 星期六 11时16分51秒
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

typedef long long lint;

int T, ca;

lint getAns(lint n) {
    set<int> st;
    for(lint i = 0; ; i++) {
        lint m = n * (i + 1);
        while(m) {
            st.insert(m % 10);
            m /= 10;
        }
        if(st.size() == 10) return (i + 1) * n;
    }
}


int main() {
    freopen("A.out", "w", stdout);
    cin >> T;
    while(T--) {
        lint n;
        cin >> n;
        cout << "Case #" << ++ ca << ": ";
        if(n == 0) {
            cout << "INSOMNIA" << endl;
        }
        else {
            cout << getAns(n) << endl;
        }
    }
    return 0;
}

