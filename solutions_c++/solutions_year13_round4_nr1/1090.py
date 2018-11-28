//#define __test__aTest__
#ifndef __test__aTest__

#include <vector>
#include <list>
#include <map.h>
#include <set.h>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <assert.h>

using namespace std;

#define ll long long

const ll MOD = 1000002013;

struct Node {
    ll o, e, p;
    bool done;
    Node() : o(0), e(0), p(0), done(false) {}
    Node(ll o, ll e, ll p) : o(o), e(e), p(p), done(false) {}
};

bool comp(Node i, Node j) { return i.o < j.o; }
int main() {
    
    freopen("/Users/zishirs/Documents/workspace/test/test/test.txt", "r", stdin);
    freopen("/Users/zishirs/Documents/workspace/test/test/output.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int index = 1; index <= T; ++index) {
        int N, M;
        cin >> N >> M;
        vector<Node> vec;
        ll o, e, p;
        for (int i = 0; i < M; ++i) {
            cin >> o >> e >> p;
            Node node(o, e, p);
            vec.push_back(node);
        }
        sort(vec.begin(), vec.end(), comp);
        ll ret = 0;
        while (true) {
            ll maxDelta = 0, dP = 0;
            int idx = 0, jdx = 0;
            for (int i = 0; i < vec.size(); ++i) {
                for (int j = 0; j < vec.size(); ++j) {
                    if (vec[i].p > 0 && vec[j].p > 0) {
                        if (vec[j].o > vec[i].o && vec[i].e < vec[j].e && vec[i].e >= vec[j].o) {
                            ll delP = min(vec[i].p, vec[j].p);
                            ll n1 = vec[j].o - vec[i].o, n2 = vec[j].e - vec[i].e;
                            if (maxDelta < n1*n2*delP) {
                                maxDelta = n1*n2*delP;
                                idx = i;
                                jdx = j;
                            }
                        }
                    }
                }
            }
            if (maxDelta == 0)
                break;
            
            dP = min(vec[idx].p, vec[jdx].p);
            if (vec[idx].p >= vec[jdx].p) {
                vec[idx].p -= dP;
                Node node1(vec[jdx].o, vec[idx].e, dP);
                vec.push_back(node1);
                vec[jdx].o = vec[idx].o;
                
            }
            else {
                vec[jdx].p -= dP;
                Node node(vec[jdx].o, vec[idx].e, dP);
                vec.push_back(node);
                vec[idx].e = vec[jdx].e;
            }
            //sort(vec.begin(), vec.end(), comp);
            ret = (ret + maxDelta % MOD) % MOD;
        }
        cout<<"Case #"<<index<<": "<<ret<<endl;
    }
    return 0;
}

#endif