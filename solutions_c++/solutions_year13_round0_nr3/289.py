#pragma comment(linker, "/STACK:33554432")

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <ctime>
#include <memory.h>

using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define ABS(n) ((n)<0 ? -(n) : (n))
#define SQR(a) (a)*(a)
#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define COPY(a,b) memcpy(a,b,sizeof (b));
#define SI(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define y1 yyyyy1
#define prev prevvvvv
#define LL long long
const double PI = 2*acos(0.0);
const double EPS = 1e-8;
const int INF = (1<<30)-1;

bool strLess (const string& a, const string& b) {
    if (a.size() != b.size()) return a.size() < b.size();
    return a < b;
}

vector<string> primes;

int fun (const string& a, const string& b) {
    int res = 0;
    vector<string>::iterator i = lower_bound (primes.begin(), primes.end(), a, strLess);
    vector<string>::iterator j = upper_bound (primes.begin(), primes.end(), b, strLess);
    return j - i;
}

int main(){
    FILE* pr = fopen ("prime.txt", "r");
    char s[200];
    while (fscanf (pr, "%s", s) != EOF) {
        string prime = string(s);
        primes.PB(prime);        
    }
    fclose (pr);

    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    sort (primes.begin(), primes.end(), strLess);
    int tc;
    cin >> tc;
    REP(ic,tc) {
        string a, b;
        cin >> a >> b;
        cout << "Case #" << ic+1 << ": " << fun (a, b) << endl;
    }
	return 0;
};