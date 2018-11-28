#include<iostream>
#include<string>
#include<set>
using namespace std;
const int NSTR = 10;
const int NSERVER = 10;


int N, M;
string s[NSTR];

void read() {
    cin >> N >> M;
    for (int i = 0; i < N; ++i)
        cin >> s[i];
}


void rec(int cur, int hist[NSTR], int &worstV, int &nWorst) {
    if (cur == N) {
        int sum = 0;
        for (int i = 0; i < M; ++i) {
            set<string> S;
            for (int j = 0; j < N; ++j)
                if (hist[j] == i) {
                    for (int k = 0; k <= s[j].size(); ++k)
                        S.insert(s[j].substr(0, k));
                }
            sum += S.size();
        }
        
        if (worstV < sum) {
            worstV = sum;
            nWorst = 1;
        }
        else if (worstV == sum) {
            ++nWorst;
        }
        return;
    }

    for (int i = 0; i < M; ++i) {
        hist[cur] = i;
        rec(cur + 1, hist, worstV, nWorst);
    }
}


void work(int cases) {
    int worstV = -1, nWorst = -1;
    int hist[NSTR];

    rec(0, hist, worstV, nWorst);

    cout << "Case #" << cases << ": " << worstV << ' ' << nWorst << endl;
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
