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

using llong = long long int;

void recur(string &s, vector<string> &res, int depth)    {
    if(depth == 0)  {
        s[depth] = '1';
        recur(s, res, depth+1);
    } else if(depth == 15)    {
        s[depth] = '1';
        res.push_back(string(s));
        return;
    } else {
        s[depth] = '0';
        recur(s, res, depth+1);
        s[depth] = '1';
        recur(s, res, depth+1);
    }

}

pair<bool,llong>  isPrime(llong x)    {
    if(x <= 1) return make_pair(false,-1);
    else if(x <= 3) return make_pair(true,-1);
    else if(x % 2 == 0 || x % 3 == 0) {
        return make_pair(false, x%2==0 ? 2 : 3);
    }


    for(llong i=5; i <= llong(ceil(sqrt((long double)x)))+1; i += 6 ) {
        if(x % i == 0)
            return make_pair(false, i);
        if(x % (i + 2) == 0)
            return make_pair(false, i+2);
    }

    return make_pair(true, -1);
}

pair<bool,vector<llong>> isJamCode(string &s)    {
    vector<llong> factors;

    for(int base=2; base <= 10; base++ )    {
        llong x = std::stoll(s, nullptr, base);
        auto p = isPrime(x);

        if(!p.first) {
            factors.push_back(p.second);
        } else  {
            factors.clear();
            return make_pair(false,factors);
        }
    }

    return make_pair(true,factors);
}

int main(int argc, char *argv[])
{
   // freopen("pancake-small.in","r",stdin);
    freopen("jamcoin-small.out","w",stdout);

    llong N = 16, J = 50;

    string s(N, '0');
    vector<string> vec;
    recur(s, vec, 0);

    cout << "Case #1:" << "\n";

    int count = 0;
    for(auto s: vec)   {
        if(count >= J) break;

        auto p = isJamCode(s);
        if(p.first) {
            count++;
            cout << s << " ";
            for(auto a: p.second)
                cout << a << " ";
            cout << "\n";
        }
    }


    return 0;
}
