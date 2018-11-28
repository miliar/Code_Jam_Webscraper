
#include <iostream>
#include <vector>

using namespace std;

int cmp(const vector<char>& A, const vector<char>& B, int L) {
    for (int l = 0; l < L; l ++) {
        if (A[l] < B[l]) return -1;
        if (A[l] > B[l]) return +1;
    }
    return 0;
}

void mv(vector<char>& A, const vector<char>& B, int S, int L) {
    for (int l = 0; l < L; l ++) {
        A[S+l] = B[l];
    }
}

bool suitable(const vector<char>& A, int P, int R, int S) {
    int p = 0;
    int r = 0;
    int s = 0;
    for (auto ch : A) {
        if (ch == 'P') p ++;
        if (ch == 'R') r ++;
        if (ch == 'S') s ++;
    }
    return (p == P && r == R && s == S);
}


int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t ++) {
        int N, R, P, S;
        cin >> N >> R >> P >> S;
        int L = R + P + S;
        vector<char> Pline(L);
        vector<char> Rline(L);
        vector<char> Sline(L);
        vector<char> newPline(L);
        vector<char> newRline(L);
        vector<char> newSline(L);
        Pline[0] = 'P';
        Rline[0] = 'R';
        Sline[0] = 'S';
        int l = 1;
        for (int n = 0; n < N; n ++) {
            if (cmp(Pline, Rline, l) < 0) {
                mv(newPline, Pline, 0, l);
                mv(newPline, Rline, l, l);
            }
            else {
                mv(newPline, Pline, l, l);
                mv(newPline, Rline, 0, l);
            }
            if (cmp(Pline, Sline, l) < 0) {
                mv(newSline, Pline, 0, l);
                mv(newSline, Sline, l, l);
            }
            else {
                mv(newSline, Pline, l, l);
                mv(newSline, Sline, 0, l);
            }
            if (cmp(Rline, Sline, l) < 0) {
                mv(newRline, Rline, 0, l);
                mv(newRline, Sline, l, l);
            }
            else {
                mv(newRline, Rline, l, l);
                mv(newRline, Sline, 0, l);
            }
            Pline.swap(newPline);
            Rline.swap(newRline);
            Sline.swap(newSline);
            l *= 2;
        }
        vector<char> best;
        if (suitable(Pline, P, R, S) && (best.size() == 0 || cmp(Pline, best, L) < 0)) {
            best = Pline;
        }
        if (suitable(Rline, P, R, S) && (best.size() == 0 || cmp(Rline, best, L) < 0)) {
            best = Rline;
        }
        if (suitable(Sline, P, R, S) && (best.size() == 0 || cmp(Sline, best, L) < 0)) {
            best = Sline;
        }
        cout << "Case #" << (t+1) << ": ";
        if (best.size() != 0) {
            for (auto ch : best) {
                cout << ch;
            }
        }
        else {
            cout << "IMPOSSIBLE";
        }
        cout << '\n';
    }
}

