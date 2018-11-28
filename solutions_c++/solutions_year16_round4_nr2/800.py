#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int N, K;
int p[1234];

vector<int> v;
double calc() {
    double ans = 0;
    for(int b = 0; b < (1<<v.size()); b++) {
        int ks = 0;
        double tmp = 1;
        for(int i = 0; i < v.size(); i++) {
            if(b & (1<<i)) {
                ks++;
                tmp *= double(v[i])/100.0;
            } else {
                tmp *= 1.0 - double(v[i])/100.0;
            }
        }
        if(ks == K/2) {
            ans += tmp;
        }
    }
    return ans;
}

double gs() {
    vector<int> vs;
    vector<int> bestv;
    double bestp = 0;
    for(int b = 0; b < (1<<N); b++) {
        vs.clear();
        for(int i = 0; i < N; i++) {
            if(b & (1<<i)) {
                vs.push_back(p[i]);
            }
        }
        if(vs.size() == K) {
            v = vs;
            double tamp = calc();
            if(bestp < tamp) {
                bestp = tamp;
                bestv = v;
            }
        }
    }
    cerr << "Best prob " << bestp << "\n";
    for(int i = 0; i < bestv.size(); i++) {
        cerr << bestv[i] << " ";
    }
    cerr << "\n";
    return bestp;
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> N >> K;
        for(int i = 0; i < N; i++) {
            string k;
            cin >> k;
            p[i] = (k[0]-'0')*100 + (k[2]-'0')*10 + (k[3]-'0');
        }
        sort(p, p + N);
        v.clear();
        for(int i = 0; i < K/2; i++) {
            v.push_back(p[i]);
            v.push_back(p[N-1-i]);
        }
        double s = calc();
        ///
        s = gs();
        ///
        cout << "Case #" << t << ": " << fixed << setprecision(7) << s << "\n";
    }
    return 0;
}
