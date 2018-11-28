#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

int n;
int mask[5];
int mask2[5];

bool solve(set<int> & all, set<int> & workers) {

    bool tmp = true;

    if (all.size() == 0) return true;

    //cout<<"hola "<<all.size()<<endl;

    set<int> s1 = all;
    set<int> s2 = workers;

    rep(it2, s2) {

        bool some = false;

        rep(it, s1) {

            //cout<<*it2<<" "<<*it<<endl;

            if (mask2[*it2]&(1<<(*it))) {



                all.erase(*it);
                workers.erase(*it2);

                //cout<<"pasa "<<all.size()<<endl;

                tmp = tmp && solve(all, workers);

                all.insert(*it);
                workers.insert(*it2);

                some = true;

            }

        }

        if (!some) return false;

    }

    return tmp;

}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {
        cin>>n;
        for (int i=0; i<n; i++) {
            string s;
            cin>>s;
            mask[i] = 0;
            for (int j=0; j<n; j++) if (s[j]=='1') {
                mask[i] |= (1<<j);
            }
        }

        int m = n*n;
        int res = n*n;
        for (int i=0; i<(1<<m); i++) {

            int c = 0;
            for (int j=0; j<n; j++) mask2[j] = mask[j];
            for (int j=0; j<n; j++) for (int k=0; k<n; k++) {
                if ((mask2[j]&(1<<k)) == 0) {
                    //cout<<"hola"<<endl;
                    if ((i & (1<<(j*n+k)))) {
                        c++;
                        mask2[j] |= (1<<k);
                    }
                }
            }

            //cout<<c<<endl;
            //cout<<mask2[0]<<" "<<mask2[1]<<endl;

            set<int> all, workers;
            for (int j=0; j<n; j++) all.insert(j);
            for (int j=0; j<n; j++) workers.insert(j);

            bool good = solve(all, workers);


            //cout<<i<<" "<<found<<" "<<one<<endl;

            if (good) {
                res = min(res, c);
            }

        }

        printf("Case #%d: %d\n", cas, res);
        cerr<<cas<<" "<<res<<endl;
    }

    return 0;

}
