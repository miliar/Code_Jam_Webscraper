#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>

#define foreach(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i) 

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

using namespace std;

int main(int argc, const char* argv[])
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, X;
        map<int, int> m;
        cin >> N >> X;
        for (int i = 0; i < N; i++) {
            int s;
            cin >> s;
            m[-s] += 1;
        }
        int ret = 0;
        while (m.size()) {
            int s = m.begin()->first;
            ret++;
            m[s]--;
            if (m[s] == 0)
                m.erase(s);
            map<int, int>::iterator it = m.lower_bound(-(X + s));
            if (it != m.end()) {
                if (it->second == 1)
                    m.erase(it->first);
                else
                    m[it->first]--;
            }
        }
        cout << "Case #" << t << ": " << ret << endl;
    }
    return 0;
}
