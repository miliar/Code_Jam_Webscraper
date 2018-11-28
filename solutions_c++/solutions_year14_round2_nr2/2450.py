#define  _CRT_SECURE_NO_DEPRECATE
#include <array>
#include <cstdio>
#include <sstream>
#include <vector>
#include <list>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <functional>
#include <cstdlib>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <map>
#include <climits>
using namespace std;

#define  print "Case #"<<t1<<": "
#define MAX 999999999999
#define pi 3.1415926535897932384626433832795028841971693993751
#define ASRT(v) (sort(v.begin(),v.end()))
#define DSRT(v) (sort(v.rbegin(),v.rend()))


template <typename T> string to_string(T num) {
    ostringstream oss;
    oss << num;
    return oss.str();
}
int stoi(string s) {
    return atoi(s.c_str());
}
long double stod(string s) {
    return atof(s.c_str());
}
vector<string> split(string s) {
    string buf;
    stringstream ss(s);
    vector<string> tokens;
    while(ss >> buf)
        tokens.push_back(buf);
    return tokens;
}
vector<int> digitFromNumber(int num) {
    vector<int> v;
    while(num > 0) {
        v.push_back(num % 10);
        num /= 10;
    }
    return v;
}
bool isPrime(long long n) {
    if(n <= 1) return false;
    if(n == 2) return true;
    if(n % 2 == 0) return false;
    long long root = sqrt((long double)n);
    for(int i = 3; i <= root; i += 2) {
        if(n % i == 0) return false;
    }
    return true;
}
long long gcd(long long a, long long b) {
    if(b == 0) return a;
    else return gcd(b, a % b);
}


typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string>vs;
typedef vector<double> vd;
typedef vector<vector<int> > vvi;



int main() {
    freopen("input.in", "r",  stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int t1 = 1; t1 <= T; t1++) {
        ll a, b, k;
        cin >> a >> b >> k;
        ll w = 0;
        for(ll i = 0; i < a; i++) {
            for(ll j = 0; j < b; j++) {
                ll r = i & j;
                if(r < k) w++;
            }
        }
        cout << print << w << endl;
    }
}
