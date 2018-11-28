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
int arr[30];
bool ok;
string ans;
string dig[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};


void solve(int idx , string s) {
    if(idx > 9)
        return;
    if(ok)
        return;
    bool b = false;
    for(int i = 0; i < 30; i ++) {
        if(arr[i]) {
            b = true;
            break;
        }
    }
    if(!b) {
        ok = true;
        ans = s;
        return;
    }
    b = false;
    for(int i = 0; i < dig[idx].size(); i ++) {
        arr[dig[idx][i]-'A'] --;
    }
    for(int i = 0; i < 30; i ++) {
        if(arr[i] < 0) {
            b = true;
            break;
        }
    }
    if(!b) {
        solve(idx , s + (char)(idx + 48));
    }
    for(int i = 0; i < dig[idx].size(); i ++) {
        arr[dig[idx][i]-'A'] ++;
    }
    solve(idx + 1 , s);
}

//#define cin in
//#define cout out
int main() {
    fstream  in("A-small-attempt1.in" , ios::in);
    fstream out("out.out" , ios::out);
    int t;
    in >> t;
    t = 100;
    string s;
    int q = 0;
    while(t --) {
        q ++;
        ok = false;
        in >> s;
        for(int i = 0; i < 30; i ++)
            arr[i] = 0;
        for(int i = 0; i < s.size(); i ++) {
            arr[s[i]-'A'] ++;
        }
        solve(0 , "");
        out << "Case #" << q << ": " << ans << endl;
    }
}
