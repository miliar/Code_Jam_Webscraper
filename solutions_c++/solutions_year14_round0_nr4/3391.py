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

int winWar(vector<double>& naomi, vector<double>& ken) {
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    vector<bool>used(ken.size(), false);
    vector<bool> naomiUse(ken.size(), false);
    int score = 0;
    for (int j = naomi.size() - 1; j >= 0;) {
        if (naomiUse[j]) {
            j--; continue;
        }
        bool canWin = false;
        REP(i, 0, ken.size()) {
            if (!used[i] && ken[i] > naomi[j]) {
                used[i] = true;
                canWin = true;
                break;
            }
        }
        if (!canWin) {
            double kenT;
            REP(i, 0, ken.size()) if (!used[i]) {
                kenT = ken[i];
                used[i] = true; break;
            }
            REP(i, 0, naomi.size()) {
                if (naomi[i] > kenT && !naomiUse[i]) {
                    naomiUse[i] = true; break;
                }
            }
            score++;
        } else {
            REP(i, 0, naomi.size()) if (!naomiUse[i]) {
                naomiUse[i] = true;
                break;
            }
        }
    }
    return score;
}

int playWar(vector<double>& naomi, vector<double>& ken) {
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    vector<bool>used(ken.size(), false);
    int score = 0;
    for (int j = naomi.size() - 1; j >= 0; j--) {
        bool canWin = false;
        REP(i, 0, ken.size()) {
            if (!used[i] && ken[i] > naomi[j]) {
                used[i] = true;
                canWin = true;
                break;
            }
        }
        if (!canWin) {
            REP(i, 0, ken.size()) if (!used[i]) {
                used[i] = true; break;
            }
            score++;
        }
    }
    return score;
}

int main() {
    clock_t startTime = clock();
    ios_base::sync_with_stdio(false);

    int T; cin>>T;
    REP(test, 1, T+1) {
        cout<<"Case #"<<test<<": ";
        int n; cin>>n;
        vector<double> naomi, ken;
        REP(i, 0, n) {
            double a; cin>>a;
            naomi.PB(a);
        }
        REP(i, 0, n) {
            double a; cin>>a;
            ken.PB(a);
        }
        int dwar = winWar(naomi, ken);
        int war = playWar(naomi, ken);
        cout<<dwar<<" "<<war<<"\n";
    }

    clock_t endTime = clock();
    cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
    return 0;
}

