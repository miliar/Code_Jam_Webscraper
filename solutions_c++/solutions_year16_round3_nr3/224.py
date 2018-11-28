#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Outfit{
    int j, p, s;
};

int J, P, S, K;
vector<Outfit> outfits;
vector<vector<int> > jp, ps, js;
vector<bool> use;
vector<bool> best_use;
int biggest_use;

void rec(int i, int n) {
    if(i == outfits.size()) {
        
        if(n > biggest_use) {
            best_use = use;
            biggest_use = n;
        }
        
        return;
    }
    
    int j = outfits[i].j;
    int p = outfits[i].p;
    int s = outfits[i].s;
    if(jp[j][p] < K && ps[p][s] < K && js[j][s] < K) {
        jp[j][p]++;
        ps[p][s]++;
        js[j][s]++;
        use[i] = true;
        rec(i+1, n+1);
        use[i] = false;
        jp[j][p]--;
        ps[p][s]--;
        js[j][s]--;
    }
    rec(i+1, n);
}

void solve() {
    cin >> J >> P >> S >> K;
    
    outfits.clear();
    
    for(int j = 0; j < J; ++j) {
        for(int p = 0; p < P; ++p) {
            for(int s = 0; s < S; ++s) {
                Outfit outfit{j, p, s};
                outfits.push_back(outfit);
            }
        }
    }
    
    jp.clear();
    ps.clear();
    js.clear();
    jp.resize(J, vector<int>(P, 0));
    ps.resize(P, vector<int>(S, 0));
    js.resize(J, vector<int>(S, 0));
    use.clear();
    use.resize(outfits.size(), false);
    biggest_use = 0;
    
    rec(0, 0);
    
    cout << biggest_use << endl;
    for(int i = 0; i < outfits.size(); ++i) {
        if(best_use[i]) {
            cout << outfits[i].j+1 << " " << outfits[i].p+1 << " " << outfits[i].s+1 << endl;
        }
    }
}

int main() {
    
    int c = 1;
    int T;
    cin >> T;
    while(T --> 0) {
        cout << "Case #" << c++ << ": ";
        solve();
    }
    
    return 0;
}
