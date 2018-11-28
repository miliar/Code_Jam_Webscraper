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

    int T; cin>>T;
    REP(test, 1, T+1) {
        int ans; cin>>ans;
        vector<int> pos;
        REP(i, 1, 5) {
            REP(j, 1, 5) {
                int p; cin>>p;
                if (ans == i) {
                    pos.PB(p);
                }
            }
        }
        cin>>ans;
        vector<int> pos2;
        REP(i, 1, 5) {
            REP(j, 1, 5) {
                int p; cin>>p;
                if (ans == i) {
                    pos2.PB(p);
                }
            }
        }
        int match = 0, card;
        REP(i, 0, pos.size()) {
            REP(j, 0, pos2.size()) {
                if (pos[i] == pos2[j]) match++, card = pos[i];
            }
        }
        cout<<"Case #"<<test<<": ";
        switch(match) {
            case 0: cout<<"Volunteer cheated!\n"; break;
            case 1: cout<<card<<"\n"; break;
            default: cout<<"Bad magician!\n"; break;
        }
    }

    clock_t endTime = clock();
    cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
    return 0;
}

