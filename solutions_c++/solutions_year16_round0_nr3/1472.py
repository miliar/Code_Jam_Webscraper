/*
ID: iamquang95
PROG: test
LANG: C++
*/

// Author: QCC
#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

//Loop
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++)
#define REP(i,a,b) for( int i=(a),_b=(b);i<_b;++i)
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
//Debugging
#define DEBUG(x) { cout << #x << " = " << x << endl; }
#define DEBUGARR(a,n) {cout << #a << " = " ; REP(_,0,n) cout << a[_] << ' '; cout <<endl;}
#define CHECK printf("OK\n");
//Read and init
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RC(X) scanf("%c", &(X))
#define DRC(X) char (X); scanf("%c", &X)
#define FILL(a, b) memset((a), (b), sizeof((a)))
//Shorten keyword
#define pb push_back
#define mp make_pair
#define st first
#define nd second

int gcd(int a, int b) { int r; while (b != 0) { r = a % b; a = b; b = r; } return a; }
int lcm(int a, int b) { return a / gcd(a, b) * b; }
int getBit(int s, int i) { return (s >> i) & 1; }
int onBit(int s, int i) { return s | (int(1) << i); }
int offBit(int s, int i) { return s & (~(int(1) << i)); }
int cntBit(int s) { return __builtin_popcount(s); }
int sqr(int x) {return x*x; };
template <typename T> string NumberToString ( T Number ) { stringstream ss; ss << Number; return ss.str();}
int StringToNumber ( const string &Text ) { stringstream ss(Text); int result; return ss >> result ? result : 0; }


typedef pair< int, int > PII;
typedef long long LL;

const int MOD = 1e9+7;
const int SIZE1 = 1e5+10;
const int SIZE2 = 1e6+10;
const int DX[4] = {-1, 1, 0, 0};
const int DY[4] = {0, 0, 1, -1};

/*long long power(long long a, long long b, long long d) {
    if (b == 0) return 1;
    if (b%2 == 0) {
        long long t = power(a, b/2, d);
        return (t*t)%d;
    } return (power(a, b-1, d)*a)%d;
}

bool rabinMiller(long long p) {
    if (p != 2 && p%2 ==0) return false;
    if (p < 2) return false;
    if (p == 2) return true;
    unsigned long long s = p-1;
    while (s%2 == 0) s >>= 1;
    for(int i = 1; i < 6; ++i) {
        long a = rand()%(p-2)+1;
        long long temp = s;long long mod = power(a, temp, p);
        while (temp != p-1 && mod != 1 && mod != p-1) {
            mod = power(mod, 2, p);
            temp <<= 1;
        }
        if (mod != p-1 && temp%2 == 0) return false;
    }
    return true;
}*/

bool rabinMiller(long long x){
    int sqrtX = (int)sqrt(x);
    FOR(i, 2, sqrtX)
        if (x%i == 0) return false;
    return true;

}

long long convertToBase(string s, int base) {
    long long result = 0;
    long long power = 1;
    for(int i = s.length()-1; i >= 0; --i) {
        result += (long long)(s[i] - '0')*power;
        power *= base;
    }
    return result;
}

int findFirstNontrivialDivisor(long long x) {
    for(int i = 2; i <= (int)sqrt(x); ++i)
        if (x%i == 0) return i;
}

void solutionSmall() {
    DRII(n, m);
    printf("\n");
    for(int i = 0; i < 16384; ++i) {
        string num = "1" + bitset<14>(i).to_string() + "1";
        bool isResult = true;
        for(int base = 2; base <= 10; ++base) {
            long long x = convertToBase(num, base);
            if (rabinMiller(x)) {
                isResult = false;
                break;
            }
        }
        if (isResult) {
            cout << num << " ";
            //cout << endl;
            for(int base = 2; base <= 10; ++base) {
                //cout << findFirstNontrivialDivisor(convertToBase(num, base)) << " " << convertToBase(num, base) << endl;
                cout << findFirstNontrivialDivisor(convertToBase(num, base)) << " ";
            }
            m--;
            if (m == 0)
                return;
            else
                printf("\n");
        }
    }
}

void solutionLarge() {
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output2.txt", "w", stdout);
    int nTest;
    scanf("%d\n", &nTest);
    for(int test = 1; test <= nTest; ++test) {
        printf("Case #%d: ", test);
        solutionSmall();
        //solutionLarge();
    }
    return 0;
}
