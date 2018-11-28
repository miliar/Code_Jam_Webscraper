#include "stdio.h"
#include "stdlib.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>
using namespace std;
bool Possible(double f) {
    for(int b=0 ; b<=40 ; b++) {
        double ipt = 1./pow(2, b);
        if(ipt<=f) {
            f-=ipt;
            if(f==0) {
                return true;
            }
        }
    }
    return false;
}
int GetGen(double f) {
    if(!Possible(f)) return -1;
    for(int b=0 ; b<=40 ; b++) {
        double ipt = 1./pow(2, b);
        if(f>=ipt) {
            return b;
        }
    }
    return -1;
}
int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int c=0;
    cin >> c;
    for(int a=0 ; a<c ; a++) {
        string s;
        string s0, s1;
        int n0, n1;
        cin >> s;
        for(int i=0 ; i<s.size() ; i++) {
            if(s[i]=='/') {
                s0 = s.substr(0, i);
                s1 = s.substr(i+1, s.size()-i-1);
            }
        }
        n0 = atoi(s0.c_str());
        n1 = atoi(s1.c_str());
        double n = double(n0)/double(n1);
        int gens = GetGen(n);
        cout << "Case #" << a+1 << ": ";
        if(gens==-1) cout << "impossible";
        else cout << gens;
        cout << endl;
    }
    return 0;
}
