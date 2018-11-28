#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <iterator>
#include <sstream>

using namespace std;

typedef vector<int> vi;
typedef vector<double> vd;

int war(int z, const vd& n_w, const vd& k_w) {
    int l=0, r=z-1, s=0;
    for (int i=z-1; i>=0; --i) {
        if (n_w[i]<k_w[r]) {
            --r;
        } else {
            ++l;
            ++s;
        }
    }
    return s;
}

int dec(int z, const vd& n_w, const vd& k_w) {
    int n=z-1, k=z-1, s=0;
    for (int i=0; i<z; ++i) {
        if (n_w[n] < k_w[k]) {
            --k;
        } else {
            --k;
            --n;
            ++s;
        }
    }
    return s;
}

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        int N;
        cin >> N;
        vd n_w(N);
        for (int i=0; i<N; ++i) cin >> n_w[i];
        sort(n_w.begin(), n_w.end(), less<double>());

        vd k_w(N);
        for (int i=0; i<N; ++i) cin >> k_w[i];
        sort(k_w.begin(), k_w.end(), less<double>());

        int dec_res = dec(N, n_w, k_w);
        int war_res = war(N, n_w, k_w);

        cout << "Case #" << cs << ": " << dec_res << " " << war_res << "\n";
    }
}
