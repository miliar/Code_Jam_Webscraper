//
//  main.cpp
//  GCJ
//
//  Created by Dung Nguyen on 5/24/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <fstream>
#include <stack>
#include <stdio.h>
#include <string.h>
#include <cassert>
#include <math.h>



#define printA(mat,n) {rep(i,n) cout << mat[i] << " "; cout << endl;}
#define printAs(mat,n,m) rep(j,n) {printA(mat[j],m)}
#define printC(col) foreach(i,col) cout << *i << " "; cout << endl;
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
#define repr(i,j,n) for (int i = (int)(n)-1; i >=(j); i--)
#define rept(i,j,n) for (int i = (j); i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define SZ(v) v.size()
#define two(p) (1 << (p))
#define twol(p) (1LL << (p))
#define contain(i,j) ((i & two(j)) != 0)
#define mp(a,b) make_pair((a),(b))
#define foreach(i,x) for (__typeof((x).begin()) i=(x).begin();i!=(x).end();i++)
#define FOR(i,l,r) for (int i=(l);i<=(r);i++)
#define ROF(i,r,l) for (int i=(r);i>=(l);i--)
#define see(var) cout << var << endl
#define ms(mat,val) memset(mat,val,sizeof(mat))
#define add push_back
#define isin(x,y,z) ((x) >= (y) && (x) =< (z))
#define reverse(mat,sz) rep(i,sz/2) swap(mat[i],mat[sz-i-1])

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> ipr;
typedef unsigned int UI;
typedef vector<int> VI;

const LL mod = 1000000007;
const char aa = 'a';
const double eps=1E-9;
const int sgn[] = {1,-1};
const LL mil = 1000000;
const LL tmil = 10000000;

template <typename T> 
void printV(vector<T> & v) {
    rep(i,v.size())
    cout << v[i] << " ";
    cout << endl;
}

template <typename T>
void printVs(vector<vector<T> > & v) {
    rep(i,v.size())
    printV(v[i]);
}

int cnt[tmil];
string toStr(LL num) {
    string res;
    while (num) {
        res += '0' + (num%10);
        num /=10;
    }
    return res;
}

bool isPalindrome(LL num) {
    string str= toStr(num);
    for(int i=0; i < str.size()/2; ++ i)
        if (str[i] != str[str.size()-1-i])
            return 0;
    return 1;
}

int main() {
    cnt[0]=0;
    for(int s=1; s < tmil; s++) {
        if (isPalindrome(s) && isPalindrome(s*s)) {
            cnt[s] = cnt[s-1] + 1;
            cout << s << " ";
        }
        else
            cnt[s] = cnt[s-1];
    }
    ifstream in("/Users/dungnguyen/Desktop/input.txt");
    ofstream out("/Users/dungnguyen/Desktop/output.txt");
    
    int T;
    in >> T;
    for (int t = 0; t < T; ++t) {
        LL A,B;
        LL a,b;
        in >> A >> B;
        a = (LL)sqrt(A);
        b = (LL)sqrt(B);
        cout <<a << " " << b << endl;
        if (a*a == A)
            --a;
        out << "Case #" << t+1 <<": " << cnt[b] - cnt[a] << endl;
        cout << "Case " << t+1 <<": " << cnt[b] - cnt[a] << endl;
    }
}

