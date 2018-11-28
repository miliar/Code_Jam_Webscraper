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

string s;
bool used[20010];

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {

        cin>>s;
        int res = 0;
        int n = s.length();
        for (int i=0; i<n; i++) used[i] = 0;
        set<pair<int,char> > all;
        for (int i=0; i<n; i++) all.insert(make_pair(i, s[i]));
        set<pair<int,char> >::iterator it = all.begin();
        set<pair<int,char> >::iterator it2, it3;;
        while (true) {

            if (it == all.end())
                break;

            it2 = it;
            it2++;

            if (it2 == all.end())
                break;

            if (it->second == it2->second) {
                res += 10;
                it3 = it;

                if (it != all.begin()) {
                    it3--;
                    all.erase(it2);
                    all.erase(it);
                    it = it3;
                }
                else {
                    all.erase(it2);
                    all.erase(it);
                    it = all.begin();
                }
            }
            else {
                it++;
            }

        }

        res += (all.size()/2)*5;

        printf("Case #%d: %d\n", cas, res);

    }

    return 0;

}
