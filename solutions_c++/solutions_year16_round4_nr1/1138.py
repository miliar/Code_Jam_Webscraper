//84104971101048411497 - Can you guess what does this mean?
using namespace std;
#include <bits/stdc++.h>
#define mapii map<int, int>
#define debug(a) cout << #a << ": " << a << endl
#define debuga1(a, l, r) fto(i, l, r) cout << a[i] << " "; cout << endl
#define fdto(i,  r, l) for(int i = (r); i >= (l); --i)
#define fto(i, l, r) for(int i = (l); i <= (r); ++i)
#define forit(it, var) for(__typeof(var.begin()) it = var.begin(); it != var.end(); it++)
#define fordit(rit, var) for(__typeof(var.rbegin()) rit = var.rbegin(); rit != var.rend(); rit++)
#define ii pair<int, int>
#define iii pair<int, ii>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define ll long long
#define maxN 13

template <class T>
T min(T a, T b, T c) {
    return min(a, min(b, c));
}

template <class T>
T max(T a, T b, T c) {
    return max(a, max(b, c));
}

char init[3] = {'R', 'S', 'P'};
int nTest, n, R, P, S, cntR, cntP, cntS;
string s[maxN];
string nullStr;

string sortRes(int i, int k) {
    if (k == 0) return nullStr+s[n][i];
    string s1 = sortRes(i, k-1);
    string s2 = sortRes(i+(1<<(k-1)), k-1);
    if (s1 < s2) return s1+s2;
    else return s2+s1;
}

int main () {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    scanf("%d", &nTest);
    fto(iTest, 1, nTest) {
        scanf("%d%d%d%d", &n, &R, &P, &S);
        //debug(iTest);
        printf("Case #%d: ", iTest);
        bool found = false;
        fto(i, 0, 2) {
            s[0] = ""; s[0] += init[i];
            fto(j, 1, n) {
                s[j] = "";
                fto(i, 0, s[j-1].length()) {
                    if (s[j-1][i] == 'R') s[j] += ((j == n-1) ? "SR" : "RS");
                    else if (s[j-1][i] == 'P') s[j] += "PR";
                    else if (s[j-1][i] == 'S') s[j] += "PS";
                }
            }
            cntP = cntR = cntS = 0;
            fto(i, 0, s[n].length()-1) {
                if (s[n][i] == 'R') ++cntR;
                else if (s[n][i] == 'P') ++cntP;
                else if (s[n][i] == 'S') ++cntS;
            }
            //printf("%d %d %d\n", cntR, cntP, cntS);
            if (cntP == P && cntR == R && cntS == S) {
                cout << sortRes(0, n);
                puts("");
                found = true;
                break;
            }
        }
        if (!found) puts("IMPOSSIBLE");
    }

    return 0;
}
