#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include "assert.h"

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

int main() {
    int np; cin>>np;
    rep(i, np){
        cout << "Case #"<<(i+1)<<": ";

        string s; cin>>s;
        int n = s.size();
        int A[n];
        rep(i, n) {
            A[i] = s[i] == '+';
        }
        
        int res=0;
        while(true) {
            int idx=-1;
            rep(i,n) {
                if(!A[i]) {
                    idx = i;
                }
            }
            if(idx == -1) {
                break;
            }

            if(idx != 0) {
                int split;
                for(split=0; ; split++) {
                    if(!A[split]) {
                        break;
                    }
                }
                if(split != 0) {
                    res++;
                    std::reverse(&A[0], &A[split]);
                    rep(i, split) {
                        A[i] = !A[i];
                    }
                }
            }
            assert(!A[0]);

            res++;
            std::reverse(&A[0], &A[idx+1]);
            rep(i, idx+1) {
                A[i] = !A[i];
            }
        }
        
        cout << res << endl;
    }
}
