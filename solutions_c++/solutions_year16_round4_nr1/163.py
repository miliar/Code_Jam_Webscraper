#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

string solve(int n, const vector<int>& v)
{
    const string rps = "RPS";

    for(int i=0; i<3; ++i){
        vector<int> x(1, i);
        while(x.size() < n){
            vector<int> y;
            for(unsigned j=0; j<x.size(); ++j){
                y.push_back(x[j]);
                y.push_back((x[j] + 2) % 3);
            }
            x.swap(y);
        }

        vector<int> w(3);
        for(int j=0; j<n; ++j)
            ++ w[x[j]];

        if(v == w){
            string s(n, ' ');
            for(int j=0; j<n; ++j)
                s[j] = rps[x[j]];
            for(int m=1; m<n; m*=2){
                string t;
                for(int i=0; i<n; i+=2*m){
                    string a = s.substr(i, m);
                    string b = s.substr(i+m, m);
                    t += min(a, b) + max(a, b);
                }
                s.swap(t);
            }
            return s;
        }
    }

    return "IMPOSSIBLE";
}

int main()
{
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        int n;
        cin >> n;
        vector<int> v(3);
        for(int i=0; i<3; ++i)
            cin >> v[i];
        string ans = solve(1<<n, v);
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}