/// in the name of ALLAH

//#include <bits\stdc++.h>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <stdio.h>
#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <deque>
#include <sstream>
#include <string>
#include <fstream>

#define bits(a) __builtin_popcount(a)
#define ll long long
int dx[] = {1 , -1 , 0 , 0 };
int dy[] = {0 ,  0 , 1 , -1};
const int mod = (int)1e9 + 7;
const int oo = 1<<30;
const ll loo = (ll)1<<60;
const double pi = 3.14159265359;
const int N = (int) 1e2 + 5;

using namespace std;

//#define in cin
//#define out cout
bool b;
int main() {
    fstream in("B-large.in" , ios::in);
    fstream out("out.out" , ios::out);
    int t , res;
    string s;
    in >> t;
    for(int q = 0; q < t; q ++) {
        in >> s;
        res = b = 0;
        for(int i = s.size()-1; i >= 0; i --) {
            if(s[i] == '-' && !b) {
                res ++;
                b = !b;
            } else if(s[i] == '+' && b) {
                res ++;
                b = !b;
            }
        }
        out << "Case #" << q+1 << ": " << res << '\n';
    }
}
