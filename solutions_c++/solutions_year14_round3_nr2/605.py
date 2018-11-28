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

vector<string> train;
int n;
#define mod 1000000007

bool isValid(string str) {
    bool valid = true;
    REP(ch, 'a', 'z'+1) {
        bool cont = true;
        REP(i, 0, str.size()) {
            if (str[i] == ch && !cont) {
                return false;
                break;
            } else if (str[i] == ch) {
                cont = false;
                int j = i;
                while (j < str.size() && str[j] == ch) {
                    j++;
                }
                i = j - 1;
            }
        }
    }
    return valid;
}

int main() {
    clock_t startTime = clock();
    ios_base::sync_with_stdio(true);

    int testCases; cin>>testCases;
    REP(tests, 1, testCases+1) {
        cout<<"Case #"<<tests<<": ";
        cin>>n;
        train.clear();
        vector<int> perm;
        perm.resize(n);
        REP(i, 0, n) {
            string str; cin>>str;
            train.PB(str);
            perm[i] = i;
        }
        bool ansPos = true;
        REP(i, 0, n) {
            if (isValid(train[i])) {
                REP(j, 1, train[i].size()) {
                    if (train[i][0] == train[i][j] ||
                        train[i].back() == train[i][j]) continue;
                    REP(k, 0, n) {
                        if (k == i) continue;
                        REP(g, 0, train[k].size()) {
                            if (train[i][j] == train[k][g]) {
                                ansPos = false;
                            }
                        }
                    }
                }
            } else ansPos = false;
        }
        if (!ansPos) {
            cout<<"0\n";
            continue;
        }
        LL ans = 0;
        do {
            //REP(i, 0, n) cout<<train[perm[i]]<<" ";
            //    cout<<"\n";
            bool ok = true;
            REP(i, 0, n) {
                if (train[perm[i]][0] == train[perm[i]].back()) {
                    continue;
                }
                REP(j, i+1, n) {
                    if (train[perm[i]][0] == train[perm[j]][0] ||
                        train[perm[i]][0] == train[perm[j]].back()) {
                            ok = false;
                            //cout<<"F f\n";
                        }
                }
            }
            REP(i, 0, n-1) {
                if (train[perm[i]].back() == train[perm[i+1]][0]) {
                    continue;
                }
                REP(j, i+1, n) {
                    if (train[perm[i]].back() == train[perm[j]][0] ||
                        train[perm[i]].back() == train[perm[j]].back()) {
                            ok = false;
                            //cout<<"S f\n";
                        }
                }
            }
            if (train[perm[n-1]].back() != train[perm[n-1]][0]) {
                //cout<<train[n-1].back()<<" "<<train[n-1][0]<<"\n";
                REP(i, 0, n-1) {
                    if (train[perm[n-1]].back() == train[perm[i]][0] ||
                        train[perm[n-1]].back() == train[perm[i]].back()) {
                            ok = false;
                            //cout<<"F R\n";
                        }
                }
            }
            if (ok) {

                ans++;
            }

        } while(next_permutation(perm.begin(), perm.end()));
        cout<<ans % mod<<"\n";;
    }

    clock_t endTime = clock();
    cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
    return 0;
}

