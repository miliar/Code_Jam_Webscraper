using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
 
#define foreach(x, v) for (typeof (v).begin() x=(v).begin(); x !=(v).end(); ++x)
#define forr(i, a, b) for (int i=(a); i<(b); ++i)
#define fore(i, a, b) for (int i=(a); i<=(b); ++i)
#define exists(e, v) find((v).begin(), (v).end(), (e))!=(v).end()
#define print(v) for (auto x=(v).begin(); x !=(v).end(); ++x) { cout << *x << " "; } cout << endl;  

typedef vector<int> vi;
 
int main(){
    freopen("D-large.in","r", stdin);
    int T;
    cin >> T;
    fore(test, 1, T){
        int N;
        cin >> N;
        vector<double> n(N), k(N);

        forr(i, 0, N)
            cin >> n[i];
        forr(i, 0, N)
            cin >> k[i];
        
        sort(n.begin(), n.end());
        sort(k.begin(), k.end());

        vector<double> na = n;
        vector<double> ka = k;


        int naive = 0,  deceit = 0;


        if(n[0] > k[N - 1]){
            naive = deceit = N;
        }
        else if (k[0] > n[N - 1]) {
            naive = deceit = 0;
        }
        else {

            // Naive
            for(auto it = na.begin(); it != na.end(); ++it) {
                auto kit = find_if(ka.begin(), ka.end(), [it] (const double& ki) { return  ki > *it; } );
                if(kit != ka.end()) {
                    //cout << "erasing " << *kit << endl;
                    ka.erase(kit); 
                } 
                else {
                    naive += ka.size();
                    break;
                }
            }

            // Smarter!
            
            sort(n.begin(), n.end());
            sort(k.begin(), k.end());

            while(k.size() > 0) {
                auto nit = find_if(n.begin(), n.end(), [&k] (const double& ni) { return  ni > k[0]; } );
                if(nit != n.end()) {
                    //cout << *nit << " > " << k[0] << endl;
                    n.erase(nit);
                    k.erase(k.begin());
                    deceit++;
                }
                else
                    break;
            }

        }
        cout << "Case #" << test << ": " << deceit << " " << naive << endl;
    }
    return 0;
}

