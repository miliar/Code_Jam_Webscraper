#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, n) for(int i=0; i<(n); ++i)
#define all(c) (c).begin(), (c).end()

int deceitfulWar(vector<double> a, vector<double> b){
    int n = (int)a.size(), res = 0;
    bool u[n];
    memset(u, 0, sizeof(u));
    rep(i, n){
        vector<double> ta(a.begin()+i, a.end()), tb;
        rep(j, n)if(!u[j])tb.push_back(b[j]);
        bool ok = true;
        rep(j, (int)ta.size()){
            if(ta[j] < tb[j]){
                ok = false;
                break;
            }
        }
        if(ok){
            res += (int)ta.size();
            break;
        }
        ok = true;
        for(int j=n-1; j>=0; --j){
            if(!u[j] && a[i] < b[j]){
                u[j] = true;
                ok = false;
                break;
            }
        }
        if(ok){
            rep(j, n)if(!u[j]){
                u[j] = true;
                break;
            }
            ++res;
        }
    }
    return res;
}

int War(vector<double> a, vector<double> b){
    int n = (int)a.size(), res = 0;
    bool u[n];
    memset(u, 0, sizeof(u));
    rep(i, n){
        bool ok = true;
        rep(j, n){
            if(!u[j] && a[i] < b[j]){
                u[j] = true;
                ok = false;
                break;
            }
        }
        if(ok){
            rep(j, n)if(!u[j]){
                u[j] = true;
                break;
            }
            ++res;
        }
    }
    return res;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; ++t){
        int N;
        scanf("%d", &N);
        vector<double> naomi(N), ken(N);
        rep(i, N)scanf("%lf", &naomi[i]);
        rep(i, N)scanf("%lf", &ken[i]);
        sort(all(naomi));
        sort(all(ken));
        printf("Case #%d: %d %d\n", t, deceitfulWar(naomi, ken), War(naomi, ken));
    }
    return 0;
}
