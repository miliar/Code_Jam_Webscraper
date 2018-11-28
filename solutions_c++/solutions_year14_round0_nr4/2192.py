/* In the name of ALLAH, most gracious, most merciful */

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cassert>
#include <set>
#include <ctime>
#include <iomanip>
#include <cstring>
#include <map>
 
using namespace std;
typedef long long ll;
typedef pair< int, int > pi;

int playWar(vector<ll> v[]){
    int ret = 0;
    set< ll >::iterator it;
    set< ll > ken(v[1].begin(), v[1].end());
    for(int i = 0; i < v[0].size(); i++){
        it = ken.lower_bound(v[0][i]);
        if(it == ken.end()) {
            ken.erase(ken.begin());
            ++ret;
        }
        else{
            ken.erase(it);
        }
    }
    return ret;
}

int playDeceitfulWar(vector<ll> v[]){
    int ret = 0;
    int i1 = 0, i2 = 0, j1 = v[0].size() - 1, j2 = v[0].size() - 1;
    for(int i = 0; i < v[0].size(); i++){
        if(v[1][j2] > v[0][j1]){ //If his highest card is higher than mine
            i1++;
            j2--;
        }else{
            ret++;
            j1--;
            j2--;
        }
    }
    return ret;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
#endif
    /*long double q;
    for(int w = 0; w < 2; w++){
        vector< long double > v;
        for(int i = 0; i < 9; i++){
            cin >> q;
            v.push_back(q);
        }
        sort(v.begin(), v.end());
        for(int i = 0; i < 9; i++){
            printf("%.3lf ", (double)v[i]);
        }
        cout << endl;
    }
    return 0;*/
    string S;
    int T, x, n, t = 1;
    cin >> T;
    while(T--){
        vector< ll > v[2];
        cin >> n;
        for(int w = 0; w < 2; w++){
            for(int i = 0; i < n; i++){
                cin >> S;
                ll cur = 0;
                int total = 0;
                for(int j = 0; j < S.size(); j++){
                    if(S[j] == '.') continue;
                    cur = cur * 10 + S[j] - '0';
                    ++total;
                }
                for(int j = total; j < 9; j++){
                    cur *= 10;
                }
                v[w].push_back(cur);
            }
            sort(v[w].begin(), v[w].end());
        }
        int y = playDeceitfulWar(v);
        int z = playWar(v);
        cout << "Case #" << t++ << ": " << y << " " << z << endl;
    }
    
    
    return 0;
}