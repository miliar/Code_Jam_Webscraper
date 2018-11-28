#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <unordered_set>
#include <utility>

using namespace std;

using uint = unsigned int;


inline uint flip(uint a, uint pos, uint N) {
    return a ^ ( ((1<<(N-pos))-1) << pos);
}


int solve(const string& s)  {

    uint N = s.length();
    uint start = std::stoi(s,nullptr,2);
    uint final = (1 << N) - 1;
    queue<pair<uint,uint>> Q;
    Q.push(make_pair(start,0));
    unordered_set<uint> inQ;
    inQ.insert(start);

    while(!Q.empty()) {
        auto x = Q.front();

//printf("first=%d, second=%d, N=%d\n",x.first, x.second, N);
        if( x.first == final)
            return x.second;

        for(uint i=0; i<N; i++)  {
            uint y = flip(x.first, i, N);
            if(inQ.find(y) == inQ.end()) {
                Q.push(make_pair(y,x.second+1));
                inQ.insert(y);
            }

        }

        Q.pop();
    }

    return -1;
}

int main(int argc, char *argv[])
{
    freopen("pancake-small.in","r",stdin);
    freopen("pancake-small.out","w",stdout);

    int T = 0;
    cin >> T;

    for(auto t=0; t < T; t++)  {
        printf("Case #%d: ", t+1);

        string s;
        cin >> s;
        std::replace( s.begin(), s.end(), '-', '0');
        std::replace( s.begin(), s.end(), '+', '1');


        int res=solve(s);

        printf("%d\n",res);

    }


    return 0;
}
