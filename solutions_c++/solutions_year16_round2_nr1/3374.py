#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;

typedef long long ll;
typedef pair<char, int> ci;
typedef vector<ci> vii;
typedef vector<int> vi;
#define INF 1000000000 // 1 billion, safer than 2B for Floyd Warshall's

// Common memset settings
//memset(memo, -1, sizeof memo); // initialize DP memoization table with -1
//memset(arr, 0, sizeof arr) // to clear array of integer


#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l;

string numarr[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

string tmp2(int i, std::map<char , int> &histogram){
    string word = "";
    bool find = true;
    string tmp = numarr[i];
    int len =tmp.length();
    
    std::map<char , int> histogram2;
    for (const char c : tmp) { ++histogram2[c]; }
    while (find){
        for (int j=0; j<len; j++){
            char t = tmp[j];
            if (histogram[t]-histogram2[t] < 0){
                find = false;
                break;
            }
        }
        if (find){
            word += to_string(i);
            for (int j=0; j<len; j++){
                histogram[tmp[j]]--;
            }
        }
    }
    return word;
}

void result(string s){
    std::map<char , int> histogram;
    

        for (const char c : s) { ++histogram[c]; }

    string word = "";
    word += tmp2(0, histogram);
    word += tmp2(2, histogram);
    word += tmp2(6, histogram);
    word += tmp2(7, histogram);
    word += tmp2(5, histogram);
    word += tmp2(8, histogram);
    word += tmp2(4, histogram);
    word += tmp2(9, histogram);
    word += tmp2(3, histogram);
    word += tmp2(1, histogram);
    
    std::sort(word.begin(), word.end());
    cout << word;
}
int main() {
    //freopen("x.in", "r", stdin);
    
    //freopen("A-small-attempt3.in", "r", stdin);
    //freopen("A-small-attempt3.out", "w", stdout);
    
   freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int tt, tn; cin >> tn;
    
    
    F1(tt,tn) {
        //cerr << tt << endl;
        string s; cin >> s;
        
        printf("Case #%d: ", tt);
        result(s);
        cout << endl;
    }
    return 0;
}
