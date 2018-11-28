#include <cstdio>
#include <cassert>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#define For(i, n) for (int i = 0; i < (int) n; ++i)
#define SIZE(x) ((int) (x).size())
#define mp(a, b) make_pair(a, b)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#ifndef DG
#define DG 0
#endif
#define LOG(...) (DG ? fprintf(stderr, __VA_ARGS__) : 0)

int main(){
    int T;
    cin >> T;
    For(cases, T) {
        int n, k;
        cin >> n >> k;
        vector <long double> probs(n);
        For(i, n) cin >> probs [i];

        vector <int> choice(n, 1);
        For(i, n - k) choice [i] = 0;
        sort(probs.begin(), probs.end());

        vector <int> bestchoice(n, -1);

        long double bestprob = 0;

        For(tries, k+1) {
            For(i, tries) {
                choice [i] = 1;
            }
            For(i, k - tries) {
                choice [n - i - 1] = 1;
            }


            vector <long double> chances(n+1, 0.0), newchances(n+1, 0.0);
            chances [0] = 1;
            For(i, n) {
                if (choice [i] == 1) {
                    For(j, n) {
                        newchances [j] += chances [j] * (1 - probs [i]);
                        newchances [j + 1] += chances [j] * probs [i];
                    }
                    For(j, n+1) {
                        chances [j] = newchances [j];
                        newchances [j] = 0.0;
                    }
                }
            }
//            For(i, n+1) cerr << chances [i] << ' ';
//            cerr << endl;
            if (bestprob < chances [k/2]) {
                bestprob =  chances [k / 2];
                bestchoice = choice;
            }

            choice.resize(0);
            choice.resize(n, 0);

        }


        double sumchosen = 0.0;
        printf("Case #%d: %.7lf\n", cases + 1, (double) bestprob);
        cerr << "chosen: ";
        For(i, n) {
            if (bestchoice [i] == 1) {
                cerr << probs [i] << ' ';
                sumchosen += probs [i];
            }
        }
        cerr << "\nothers: ";
        For(i, n) {
            if (bestchoice [i] == 0) cerr << probs [i] << ' ';
        }
        cerr << endl << sumchosen << endl;
    }

}
