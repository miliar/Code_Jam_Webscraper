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
bool b[10];
int main() {
    fstream in("A-large.in" , ios::in);
    fstream out("out.out" , ios::out);
    int t , n;
    in >> t;
    for(int q = 0; q < t; q ++) {
        in >> n;
        bool ok;
        memset(b , 0 , sizeof b);
        for(int i = 1,tmp; i <= (int)1e6; i ++) {
            tmp = i*n;
            while(tmp > 0) {
                b[tmp%10] = 1;
                tmp /= 10;
            }
            ok = true;
            for(int j = 0; j < 10; j ++)
                if(!b[j]) {
                    ok = false;
                    break;
                }
            if(ok) {
                out << "Case #" << q + 1 << ": " << i*n << '\n';
                break;
            }
        }
        if(!ok)
            out << "Case #" << q + 1 << ": INSOMNIA\n";
    }
}
