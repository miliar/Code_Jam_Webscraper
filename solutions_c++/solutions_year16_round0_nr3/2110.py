#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <time.h>
#include <bitset>
#include <cmath>
#include "ttmath.h" //Source from http://www.ttmath.org

typedef int jnt;
#define int long long

#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define DEB(x) cerr << x << '\n';
#define endl '\n'

#define bigint ttmath::Int<2>

using namespace std;


jnt main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    srand(time(0));
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        int n, ju;
        cin >> n >> ju;
        int until = (1 << (n - 2)); //all possible jamcodes 1 & string(i..until) & 1
        vector<int> primesI = {2,3};
        for(int i = 6; i <= 100000; i += 6) {
            bool success = true;
            for(int j = 0; j < primesI.size() && primesI[j] <= sqrt(i+1); ++j)
                if((i-1) % primesI[j] == 0) success = false;
            if(success) primesI.push_back(i-1);
            success = true;
            for(int j = 0; j < primesI.size() && primesI[j] <= sqrt(i+1); ++j)
                if((i+1) % primesI[j] == 0) success = false;
            if(success) primesI.push_back(i+1);
        }
        vector<bigint> primes;
        for(int i = 0; i < primesI.size(); ++i) {
            bigint aw = to_string(primesI[i]);
            primes.push_back(aw);
        }
        vector<pair<string, vector<bigint> > > jNums;
        for(int j = 0; j < until && jNums.size() < ju; ++j) {
            string str = "";
            if(n == 32) str = "1" + bitset<30>(j).to_string() + "1";
            else /*if(n==16)*/ str = "1" + bitset<14>(j).to_string()+ "1";
            //if(j % 1000000 == 0) cout << str << endl;
            vector<bigint> used (11-2,-1);
            bool success = true;
            for(jnt b = 2; b <= 10; ++b) {
                bigint big;
                big.FromString(str,b);
                for(int k = 0; k < primes.size(); ++k) {
                    if(big % primes[k] == 0) {
                        used[b-2] = primes[k];
                        break;
                    }
                }
                if(used[b-2] == -1) {success = false; break; }
            }
            if(success) jNums.push_back({str,used});
        }
        cout << "Case #" << i << ":" << endl;
        for(int j = 0; j < jNums.size(); ++j) {
            cout << jNums[j].first << ' ';
            for(int k = 0; k < jNums[j].second.size(); ++k) cout << jNums[j].second[k] << " ";
            cout << endl;
        }
    }
    return 0;
}
