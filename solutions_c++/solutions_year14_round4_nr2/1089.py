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
        vector<int> num, perm;
        map<int, int> MP;
        REP(i, 0, n) {
            int p; cin>>p;
            num.PB(p);
            MP[p] = i;
        }
        sort(num.begin(), num.end());
        int ans = (1<<29);
        do {
            auto cur = num;
            bool ok = true;
            int m = cur.size();
            REP(i, 0, cur.size()-1) {
                if (cur[i] < cur[i+1]);
                else {
                    m = i;
                    break;
                }
            }
            REP(i, m, cur.size()-1) {
                if (cur[i] > cur[i+1]);
                else ok = false;
            }
            if (ok) {
                REP(i, 0, cur.size()) {
                    cur[i] = MP[cur[i]];
                }
                int curd = 0;
                REP (i, 0, cur.size()) {
                    REP(j, 0, cur.size() - 1) {
                        if (cur[j] > cur[j+1]) {
                            swap(cur[j], cur[j+1]);
                            curd++;
                        }
                    }
                }
                ans = min(ans, curd);
//                cout<<curd<<"\n";
//                for (auto e:cur) cout<<e<<" ";
//                cout<<"\n\n";
            }
        } while(next_permutation(num.begin(), num.end()));
        cout<<ans<<"\n";
    }

    clock_t endTime = clock();
    cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
    return 0;
}

