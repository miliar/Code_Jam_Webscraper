#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

struct A {
    int freq;
    int index;
    bool operator<(const A& a) const {
        return freq> a.freq;
    }
};
typedef long long ll;
typedef unsigned int uint;
#define forn(i,n) for(i=0;i<(n);i++)
template<typename T> ostream &operator <<(ostream &os, const vector<T> &v) {
    copy(v.begin(), v.end(), ostream_iterator<T>(os, " "));
    return os;
}

int main(int argc, char *argv[]) {

    if(DEBUG) freopen("input.txt","r",stdin);

    uint TT, TC;
    scanf("%d", &TT);
    forn(TC,TT) {
        int n;
        cin >> n;
        vector<A> S(n);
        for(int i=0;i<n;i++) {
            int f;
            cin >> f;
            S[i].freq = f;
            S[i].index = i;
        }

        string ans;
        while(S.size()) {
            sort(S.begin(),S.end());

            if(ans.length()>0) 
                ans+= ' ' ;
            int c = 1;
            for(int i=0;i<S.size();i++) 
                if(i!=0 && S[0].freq == S[i].freq) c++;
            if(c==2)  {
                S[0].freq--;
                S[1].freq--;
                ans += ('A'+S[0].index);
                ans += ('A'+S[1].index);
                if(S[0].freq == 0) S.erase(S.begin());
                if(S[0].freq == 0) S.erase(S.begin());
            } else {
                if(S[0].freq == 2 && S.size()==1) {
                    ans += ('A'+S[0].index);
                    ans += ('A'+S[0].index);
                    S.erase(S.begin());
                } else {
                    S[0].freq--;
                    ans += 'A'+S[0].index;
                    if(S[0].freq == 0) S.erase(S.begin());
                }
            }
        }
        cout << "Case #" << TC+1 << ": " << ans << endl;
    }
    return 0;
}
