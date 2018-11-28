/***********************************************
* Author - LUONG VAN DO                        *
* Problem 
* Algorithm
* Time Limit
* *********************************************/
#include <iostream>
#include <stdio.h>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <math.h>
#include <cstring>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

#define FileIn(file) freopen(file".inp", "r", stdin)
#define FileOut(file) freopen(file".out", "w", stdout)
#define fr(i,a,b) for (int i=a;i<=b;i++)
#define FORD(i,a,b) for (int i=a;i>=b;i--)
#define rep(i, n) for (int i=0; i<n; i++)
#define repr(i, n) for (int i = n - 1;i >= 0;i--)
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define pb push_back
#define ff first
#define ss second
#define PI 3.1415926535897932385
#define uint64 unsigned long long
#define int64 long long
#define INF 500000000
#define N 100111
#define MAX_LOG 20
using namespace std;

inline int max(int a, int b) { return a > b ? a : b; }
inline int min(int a, int b) { return a < b ? a : b; }
inline int gcd(int a, int b) { if (a % b) return gcd(b, a % b); else return b; }
inline int lcm(int a, int b) { return (a * (b / gcd(a, b) )); }

inline int And(int mask, int bit) { return mask & (1 << bit); }
inline int Or(int mask, int bit) { return mask | (1 << bit); }
inline int Xor(int mask, int bit) { return mask & (~(1 << bit)); }

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
int cases;
int L, X, m;
string str, s;
char posi, posj, posk;
int negi, negj, negk, f[N];
bool isOk;
vector <int> pi;
char multi(char x, char y, int &neg) {
    if (x == '1') {
        if (y == '1') return '1';
        if (y == 'i') return 'i';
        if (y == 'j') return 'j';
        if (y == 'k') return 'k';
    }
    if (x == 'i') {
        if (y == '1') return 'i';
        if (y == 'i') {
            neg ^= 1;
            return '1';
        }
        if (y == 'j') return 'k';
        if (y == 'k') {
            neg ^= 1;
            return 'j';
        }
    }
    if (x == 'j') {
        if (y == '1') return 'j';
        if (y == 'i') {
            neg ^= 1;
            return 'k';
        }
        if (y == 'j') {
            neg ^= 1;
            return '1';
        }
        if (y == 'k') return 'i';
    }
    if (x == 'k') {
        if (y == '1') return 'k';
        if (y == 'i') return 'j';
        if (y == 'j') {
            neg ^= 1;
            return 'i';
        }
        if (y == 'k') {
            neg ^= 1;
            return '1';
        }
    }
}
int main() {
	freopen("exam.inp","r", stdin); freopen("exam.out","w", stdout);
	int caseno = 0;
    scanf(" %d ", &cases);
    while (cases--) {
        cin >> L >> X;
        s = "";
        cin >> str; pi.clear();
        for (int i = 0;i < X;i++) s += str;
        m = s.size();
        for (int i = 0;i < m;i++) f[i] = 0;
        posi = s[0]; negi = 0;
        for (int i = 1;i < m;i++) {
            if (posi == 'i' && negi == 0) pi.pb(i);
            posi = multi(posi, s[i], negi);
        }
        posk = s[m - 1]; negk = 0;
        for (int i = m - 2;i >= 0;i--) {
            if (posk == 'k' && negk == 0) f[i + 1] = 1;
            posk = multi(s[i], posk, negk);
        }
        /*cout<<s<<endl;
        for (int i = 0;i < pi.size();i++) cout<<pi[i]<<endl;
        cout<<endl;
        for (int i = 0;i < m;i++)
            if (f[i]) cout<<i<<endl;*/
        isOk = false;
        printf("Case #%d: ", ++caseno);
        if (pi.size() == 0) puts("NO");
        else {
            for (int i = 0;i < pi.size() && !isOk;i++) {
                posj = s[pi[i]]; negj = 0;
                for (int j = pi[i] + 1;j < m && !isOk;j++) {
                    if (posj == 'j' && negj == 0 && f[j])
                        isOk = true;
                    posj = multi(posj, s[j], negj);
                }
            }
            if (isOk) puts("YES");
            else puts("NO");
        }
    }
	return 0;
}
