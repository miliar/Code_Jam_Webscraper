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

int battle(int a, int b) {
    if (a == b) {
        cerr << "Something happened\n";
        exit(1);
    }
    if ((a + 1) % 3 == b) return a;
    return b;
}

char candidates[3] = {'P', 'R', 'S'};

void printrecursive(int round, int candidate/*, vector <vector <int> >& permutations, vector <vector <vector <int> > >& usage*/) {
    if (round == 0) {
        printf("%c", candidates [candidate]);
        return;
    }
    if (candidate == 0) {
        printrecursive(round - 1, 0);
        printrecursive(round - 1, 1);
    }
    else if (candidate == 1) {
        printrecursive(round - 1, 0);
        printrecursive(round - 1, 2);
    }
    else {
        printrecursive(round - 1, 1);
        printrecursive(round - 1, 2);
    }
}

int main(){
    int T;
    cin >> T;
    For(cases, T) {
        int n;
        cin >> n;
        vector <vector <int> > permutations(n+1, vector <int> (3, 0));
        permutations [0] [1] = 1;
        permutations [0] [2] = 2;
        vector <vector <vector <int> > > usage(n+1, vector <vector <int> > (3, vector <int> (3, 0)));   // 1: round, 2: result, 3: resource
        usage [0] [0][0] = 1;
        usage [0] [1] [1] = 1;
        usage [0] [2] [2] = 1;

        for (int i = 1; i <= n; i++) {
            permutations [i] [0] = battle(permutations [i - 1] [0], permutations [i - 1] [1]);
            permutations [i] [1] = battle(permutations [i - 1] [0], permutations [i - 1] [2]);
            permutations [i] [2] = battle(permutations [i - 1] [1], permutations [i - 1] [2]);

            For(j, 3) {
                usage [i] [permutations [i] [0]] [j] = usage [i - 1] [permutations [i - 1] [0]] [j] + usage [i - 1] [permutations [i - 1] [1]] [j];
                usage [i] [permutations [i] [1]] [j] = usage [i - 1] [permutations [i - 1] [0]] [j] + usage [i - 1] [permutations [i - 1] [2]] [j];
                usage [i] [permutations [i] [2]] [j] = usage [i - 1] [permutations [i - 1] [1]] [j] + usage [i - 1] [permutations [i - 1] [2]] [j];
            }
        }
        vector <int> counts(3);
        bool written = false;
        cin >> counts [1] >> counts [0] >> counts [2];

        printf("Case #%d: ", cases + 1);
        For(i, 3) {
            bool same = true;
            For(j, 3) {
                if (counts [j] != usage [n] [permutations [n] [i]] [j]) same = false;
            }
            if (same) {
                written = true;
                printrecursive(n, i/*, permutations, usage*/);
                break;
            }
        }
        if (!written) printf("IMPOSSIBLE");
        printf("\n");
        
    }

}
