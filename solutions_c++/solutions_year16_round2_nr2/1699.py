/// in the name of ALLAH

///#include <bits\stdc++.h>

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
#include <utility>

#define bits(a) __builtin_popcount(a)
#define ll long long
int dx[] = {1 , -1 , 0 , 0 };
int dy[] = {0 ,  0 , 1 , -1};
const int mod = (int)1e9 + 7;
const int oo = 1<<30;
const ll loo = (ll)1<<60;
const double pi = 3.14159265359;
const int N = (int) 1e6 + 5;

using namespace std;
string a , b;
string aans , bans;
int diff = oo;


int toInt(string s) {
    stringstream ss;
    int n;
    ss << s;
    ss >> n;
    return n;
}
void solve(int idx) {
    if(idx == a.size()) {
        int res = abs(toInt(a) - toInt(b));
        if(res < diff) {
            diff = res;
            aans = a;
            bans = b;
        }
        return;
    }
    if(a[idx] != '?' && b[idx] != '?') {
        solve(idx+1);
    } else if(a[idx] == '?' && b[idx] == '?') {
        for(char i = '0'; i <= '9'; i ++) {
            a[idx] = i;
            for(char j = '0'; j <= '9'; j ++){
                b[idx] = j;
                solve(idx + 1);
            }
        }
        a[idx] = b[idx] = '?';
    } else if(a[idx] == '?') {
        for(char j = '0'; j <= '9'; j ++){
            a[idx] = j;
            solve(idx + 1);
        }
        a[idx] = '?';
    } else {
        for(char j = '0'; j <= '9'; j ++){
            b[idx] = j;
            solve(idx + 1);
        }
        b[idx] = '?';
    }
}

//#define in cin
//#define out cout
int main() {
    fstream  in("B-small-attempt0.in" , ios::in);
    fstream out("out.out" , ios::out);
    int t;
    in >> t;
    int q = 0;
    while(t --) {
        q++;
        diff = oo;
        in >> a >> b;
        solve(0);
        out << "Case #" << q << ": " << aans << " " << bans << endl;
    }
}
