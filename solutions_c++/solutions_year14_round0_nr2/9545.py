// uva 11289
#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <string>
#include <queue>
#include <fstream>
#include <map>

#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DR(i,a) for(int i = (a)-1; i >=0; i--)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORD(i,a,b) for(int i = (a), _b = (b); i >= _b; i--)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define PB push_back
#define MP make_pair

#define F first
#define S second
#define RESET(c,x) memset(c,x,sizeof(c))
#define SIZE(c) (c).size()
#define ALL(c) (c).begin(), (c).end()

#define REP(i,a) for(int i = 0; i < (a); i++)

#define sqr(x) ((x)*(x))
#define oo 1000000009
using namespace std;
/*************************TEMPLATE**********************************/
long long convertToNum(string s)
{
    long long val = 0; FR(i,s.size()) val = val * 10 + s[i] - '0';
    return val;
}
char bu[50];
string convertToString(int a) {
    sprintf(bu,"%d",a);
    return string(bu);
}
long long GCD(long long x,long long y)  {
    if (!x) return y; if (!y) return x;
    if (x == y) return x; if (x < y) return GCD(x,y%x); else return GCD(x%y,y);
}
long long POW(long long x,long long y,long long Base){
    if (!y) return 1; long long u = POW(x,y/2,Base);
    u = (u * u) % Base;
    if (y & 1) return (u * x) % Base; else return u;
}
void extended_euclid(long long A, long long B, long long &x,long long &y) {
    if (A == 1 && B == 0) {
        x = 1;
        y = 0;
        return;
    }
    if (A < B) extended_euclid(B,A,y,x);
    else {
        long long xx,yy;
        extended_euclid(A%B,B,xx,yy);
        x = xx;
        y = yy - (A/B)*xx;
        
    }
}
//newstate = (newstate-1) & oldstate
/**************************CODE HERE*****************************/


int N, tmp, Count=0, have1, save, line1, line2;
double C, F, X;
vector<int> v;
std::map<int, int> myMap;

double findT(double curSpd, double curT, int curCookie, double result) {
    if (curCookie >= X) return curT;
    result = min(result, curT + (X - curCookie)/curSpd);
    double t = result;
    double nextSpd = curSpd + F, nextT = curT + max((double)0,(C - curCookie)/curSpd);
    double nextCookie = max((double)0,curCookie - C), nextResult = min(result, nextT + (X - nextCookie)/nextSpd);
    if (nextResult < result)
    if (max((double)0,(C - curCookie)/curSpd) <= (X - curCookie)/curSpd)
        t = findT(nextSpd, nextT, nextCookie, result);
    result = min(result, t);
    return result;
}

int main() {
    string st;
    freopen("in2.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> N;
    while (N--) {
        Count++;
        cout << "Case #" << Count << ": ";
        cin >> C >> F >> X;
        printf("%.7f\n", findT(2, 0, 0, 100000/2));
    }    
    return 0;
}
