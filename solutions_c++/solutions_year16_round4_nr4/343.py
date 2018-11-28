#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define TWO(x) (1LL<<(x))

using namespace std;

bool test(vector<vector<bool>> stuff) {
    bool ok = true;

    int n = stuff.size();

    sort(stuff.begin(), stuff.end());

    bool used[4];
    do {


        int pick[4];
        for(pick[0] = 0; pick[0] < 4; pick[0]++) {
        for(pick[1] = 0; pick[1] < 3; pick[1]++) {
        for(pick[2] = 0; pick[2] < 2; pick[2]++) {
        for(pick[3] = 0; pick[3] < 1; pick[3]++) {

            rep(i, 4) {
                used[i] = false;
            }
            rep(i, n) {
                bool got = false;
                int acc=0;
                rep(k, n) {
                    if(stuff[i][k] && !used[k]) {
                        if(acc == pick[i]) {
                            used[k] = true;
                            got = true;
                            break;
                        }
                        acc++;
                    }
                }
                if(!got) {
                    if(pick[i] != 0) {
                        break;
                    } else {
                        ok = false;
                    }
                }
            }

        }
        }
        }
        }

    } while(next_permutation(stuff.begin(), stuff.end()));

    return ok;
}

void show(vector<vector<bool> > v) {
    rep(i, v.size()) {
        rep(k, v.size()) {
            cout << v[i][k];
        }
        cout << endl;
    }
    cout << endl << endl;

}


int main() {
    int np; cin>>np;
    rep(i, np){
        int n; cin>>n;

        vector<vector<bool>> in;
        rep(i, n) {
            vector<bool> temp(n);
            string s; cin>>s;
            rep(k,n) {
                temp[k] = (s[k] == '1');
            }
            in.push_back(temp);
        }

        int res = 1e9;
        rep(seed, TWO(n*n)) {
            vector<vector<bool> > copy = in;
            int cnt = 0;
            rep(i, n) {
                rep(k, n) {
                    if(seed & TWO(i*n+k)) {
                        copy[i][k] = true;
                        cnt++;
                    }
                }
            }
            if(test(copy)) {
                res = min(res, cnt);
            }
        }
        
        cout << "Case #"<<(i+1)<<": ";
        cout << res << endl;
    }
}
