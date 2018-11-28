#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>
#include <ctime>
#include <climits>
#include <iomanip>
#include <sstream>
using namespace std;

typedef long long LL;
#define tr(container, it)for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

int main() {
    clock_t startTime = clock();
    ios_base::sync_with_stdio(false);

    int ttt; cin>>ttt;
    REP(test, 1, ttt+1) {
        cout<<"Case #"<<test<<": ";
        int a, b, k;
        cin>>a>>b>>k;
        LL ans = 0;
        REP(i, 0, a) {
            REP(j, 0, b) {
                int val = i & j;
                if (val < k) ans++;
            }
        }
        cout<<ans<<"\n";
    }

    clock_t endTime = clock();
    cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
    return 0;
}

