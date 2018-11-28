#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
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

int solve(const vector<vector<int> >& v, int m)
{
    int n = v.size();
    int ans = INT_MAX;
    for(int i=0; i<(1<<n); ++i){
        bitset<32> bs(i);
        if(bs[0] || !bs[1])
            continue;

        vector<int> wordType(m, 0);
        for(int j=0; j<n; ++j){
            for(unsigned k=0; k<v[j].size(); ++k){
                if(bs[j])
                    wordType[v[j][k]] |= 1;
                else
                    wordType[v[j][k]] |= 2;
            }
        }
        ans = min(ans, count(wordType.begin(), wordType.end(), 3));
    }

    return ans;
}

int main()
{
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        int n;
        cin >> n;
        cin.ignore();

        vector<vector<int> > v(n);
        map<string, int> m;
        for(int i=0; i<n; ++i){
            string s;
            getline(cin, s);
            istringstream iss(s);

            for(;;){
                string t;
                if(!(iss >> t))
                    break;
                if(m.find(t) == m.end()){
                    int j = m.size();
                    m[t] = j;
                }
                v[i].push_back(m[t]);
            }
        }

        int ans = solve(v, m.size());
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}