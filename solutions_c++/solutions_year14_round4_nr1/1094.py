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
    ios_base::sync_with_stdio(true);

    int testCases; cin>>testCases;
    REP(tests, 1, testCases+1) {
        cout<<"Case #"<<tests<<": ";
        int n; cin>>n;
        int x; cin>>x;
        vector<int> fi;
        REP(i, 0, n) {
            int s; cin>>s;
            fi.PB(s);
        }
        sort(fi.begin(), fi.end());
        int ans = 0;
        int fr = 0, en = n-1;
        while (fr <= en) {
            //cout<<fr<<" "<<en<<"\n";
            int sz = fi[en];
            int tsz = sz + fi[fr];
            if (fr == en) tsz -= fi[fr];
            if (tsz <= x) {
                fr++;
                en--;
                ans++;
            } else {
                en--;
                ans++;
            }
            //cout<<fr<<" "<<en<<"\n";
        }
        cout<<ans<<"\n";
    }

    clock_t endTime = clock();
    cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
    return 0;
}

