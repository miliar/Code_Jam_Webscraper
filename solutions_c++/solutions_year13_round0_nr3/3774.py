/* 
 * File:   main.cpp
 * Author: a.elbashandi
 *
 * Created on April 13, 2013, 11:58 AM
 */

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define pi acos(-1.0)
#define N 1000000
#define LL long long

#define For(i, a, b) for( int i = (a); i < (b); i++ )
#define Fors(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fore(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Set(a, s) memset(a, s, sizeof (a))
#define Read(r) freopen(r, "r", stdin)
#define Write(w) freopen(w, "w", stdout)

using namespace std;

/*
 * 
 */

bool check_palind(long n){
    stack<long> s;
    long size = (long) log10(n) + 1;
    int m, d;
    
    d = size/2 - 1;
    
    long temp = n;
    for (int i = 0; i <= d; i++) {
        m = temp % 10;
        s.push(m);
        temp /= 10;
    }
    
    if(size % 2 != 0)
        temp /= 10;
    
    bool perfect = true;
    while(temp && !s.empty() && perfect){
        m = temp % 10;
        if(m != s.top())
            perfect = false;
        s.pop();
    }
    
    return perfect;
}

int main(int argc, char** argv) {
    
    Read("C-small-attempt0.in");
    Write("file.out");
    
    vector<long> v;
    
    for (long i = 1; i <= 1000; i++) {
        if(check_palind(i) && check_palind(i * i)){
            v.push_back(i * i);
        }
    }

    
    int T, cases = 1; scanf("%d", &T);
    while(T--){
        int a, b;
        scanf("%d %d", &a, &b);
        
        int counter = 0;
        for (int i = 0; i < v.size(); i++) {
            if(v[i] >= a && v[i] <= b)
                counter++;
        }
        
        printf("Case #%d: %d\n", cases++, counter);
    }
    return 0;
}

