#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <cctype>

#define FOR(i,n) for(long long int i=0; i<n; i++)
#define MP(a,b) make_pair(a,b)
#define PB(x) push_back(x)
#define SORT(a) sort(a.begin(), a.end())
#define REV(a) reverse(a.begin(), a.end())

#define COND(p,t,f) ((p)?(t):(f))

#define PI 3.14159265

using namespace std;
typedef long long int lint;
typedef unsigned long long int ulint;



int main() {
    int T;
    cin >> T;
    FOR(t,T) {
        ulint X,N;
        cin >> N >> X;
        vector <ulint> a(N);
        FOR(i,N) cin >> a[i];
        SORT(a);
        int res = 0;
        int i=0, j=N-1;
        while (i<j) {
            if (a[i]+a[j]<=X) {
                i++; j--;
                res++;
            }
            else {
                j--;
                res++;
            }
        }
        if (i==j) res++;
        cout << "Case #" << t+1 << ": ";
        cout << res << endl;
    }

}
