#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

struct st {
    int A, B, C;
    
};

int main() {
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
        int n, A, B, C; cin >> n >> A >> B >> C;
        bool poss = true;

        while (A+B+C > 1) {
            int DA_ = (B-C+A), DB_ = (B+C-A), DC_ = (-B+C+A);
            int A_ = A-DA_/2, B_ = B-DB_/2, C_ = C-DC_/2;
            if (A_ < 0 || B_ < 0 || C_ < 0 || (A_ + B_ + C_) != (A+B+C)/2) {
                poss = false;
                break;
            }
            A = A_;
            B = B_;
            C = C_;
        }
        cout << "Case #" << ca << ": ";
        if (!poss) cout << "IMPOSSIBLE" << endl;
        else {
            string s = "";
            s.push_back("RPS"[A*0 + B*1 + C*2]);
            for (int l = 0; l < n; l++) {
                string s_ = "";
                for (int i = 0; i < s.size(); i++) {
                    char c = s[i];
                    if (c == 'R') {
                        s_ += "RS";
                    } else if (c == 'P') {
                        s_ += "PR";
                    } else if (c == 'S') {
                        s_ += "PS";
                    }
                }
                s = s_;
            }
            

            //cerr << s << endl;
            int dx = 1;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < s.size(); j+=2*dx) {
                    if (s.substr(j, dx) > s.substr(j+dx, dx)) {
                        for (int k = 0; k < dx; k++) {
                            swap(s[j+k], s[j+dx+k]);
                        }
                    }
                }
                dx *= 2;
                //cerr << s << endl;
            }
            
            cout << s << endl;
        }
    }
    return 0;
}